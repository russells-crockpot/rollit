"""
"""
import inspect
import operator
import sys
from collections import ChainMap

from . import model
from .exceptions import InvalidNameError, RollItSyntaxError, NoSuchLoopError, RollItTypeError, \
        NoneError, CannotReduceError
from .internal_objects import Reducable, Roll
from .towers import DefaultTower

if sys.version_info.minor >= 8:
    from functools import cached_property
else:
    cached_property = property

__all__ = ['ExecutionEnvironment', 'ExecutionContext', 'NoSubject', 'Scope']


def _raise_not_implemented(*args):
    raise NotImplementedError


_OPERATOR_MAP = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
    '//': operator.truediv,
    '%': operator.mod,
    '&': _raise_not_implemented,
    '^': _raise_not_implemented,
    '>': operator.gt,
    '<': operator.lt,
    '==': operator.eq,
    '!=': operator.ne,
    '>=': operator.ge,
    '<=': operator.le,
    'has': lambda x, y: y in x,
    'and': operator.and_,
    'or': operator.or_,
}


class Scope:
    """
    """

    # pylint: disable=protected-access
    def __init__(self, parent=None, *, isolate=False):
        """
        :param parent: The parent scope.
        :param bool isolate: When a scope is isolated, any values assigned will not override the
            values of the parent scope.
        """
        self._parent = parent
        self._isolated = isolate
        if not self._parent:
            self._loops = ChainMap()
            self._variables = ChainMap()
        else:
            self._loops = ChainMap({}, *self._parent._loops.maps)
            if not self._isolated:
                self._variables = ChainMap({}, *self._parent._variables.maps)
            else:
                self._loops = ChainMap()

    def add_loop(self, name, loop):
        """
        """
        self._loops[name] = loop

    def get_loop(self, name):
        """
        """
        try:
            return self._loops[name]
        except KeyError:
            raise NoSuchLoopError(name) from None

    def __contains__(self, key):
        return key in self._variables

    def __getitem__(self, name):
        try:
            return self._variables[name]
        except KeyError:
            raise InvalidNameError(name) from None

    def __setitem__(self, name, value):
        if self._parent and not self._isolated and name in self._parent:
            self._parent[name] = value
        self._variables[name] = value


class ExecutionEnvironment:
    """
    """

    def __init__(self, parser, *, dice_tower=DefaultTower):
        if inspect.isclass(dice_tower):
            dice_tower = dice_tower()
        self.dice_tower = dice_tower
        self._context = ExecutionContext(env=self)
        self._parser = parser

    def evaluate(self, stmt):
        """
        """
        stmt_model = self._parser.parse(stmt)[0]
        return self._context.evaluate(stmt_model)


def __create_no_subject():

    class _NoSubjectBase(tuple):
        __the_object = None

        def __new__(cls):
            if not cls.__the_object:
                cls.__the_object = super().__new__(cls)
            return cls.__the_object

        def __bool__(self):
            return False

    return _NoSubjectBase()


NoSubject = __create_no_subject()
""" """
del __create_no_subject


class ExecutionContext:
    """
    """
    _evaluators = ChainMap()
    _reducers = ChainMap()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._reducers = cls._evaluators = None
        for b in cls.__bases__:
            if issubclass(b, ExecutionContext):
                # pylint: disable=protected-access,no-member
                cls._evaluators = b._evaluators.new_child()
                cls._reducers = b._reducers.new_child()
                break

    def __init__(self, *, subject=NoSubject, loop=None, env=None, _parent=None):
        self._parent = _parent
        self._env = env or self._parent._env
        self._loop = loop
        self.__subject = subject
        if not self._parent:
            self._scope = Scope()
        #TODO Consider scopes and modifier calls and defs
        elif self.in_modifier and not self._parent.in_modifier:
            self._parent = self._scope = Scope(self._parent.root, isolate=True)
            self._parent = self._parent.root
        else:
            self._scope = Scope(self._parent._scope)

    @classmethod
    def reducer(cls, obj_type):
        """
        """

        def _decorator(func):
            cls._reducers[obj_type] = func
            return func

        return _decorator

    @classmethod
    def evaluator(cls, obj_type):
        """
        """

        def _decorator(func):
            cls._evaluators[obj_type] = func
            return func

        return _decorator

    @property
    def subject(self):
        """
        """
        return self.__subject

    @subject.setter
    def subject(self, value):
        if value is NoSubject and self.__subject is not NoSubject:
            raise ValueError('Cannot delete a subject after context creation!')
        self.__subject = value

    @cached_property
    def root_loop(self):
        """
        """
        if self._parent and self._parent.root_loop:
            return self._parent.root_loop
        return self._loop

    @cached_property
    def current_loop(self):
        """
        """
        if self._loop or not self._parent:
            return self._loop
        return self._parent.current_loop

    @cached_property
    def in_modifier(self):
        """
        """
        return self.__subject is not NoSubject

    @cached_property
    def root(self):
        """
        """
        if self._parent:
            return self._parent.root
        return self

    def create_child(self, subject=None, loop=None):
        """
        """
        return type(self)(subject=subject, loop=loop, _parent=self)

    def get_loop(self, name):
        """
        """
        if name == model.SpecialReference.NONE:
            return self.current_loop
        if name == model.SpecialReference.ROOT:
            return self.root_loop
        return self._scope.get_loop(name)

    def __getitem__(self, name):
        if name == model.SpecialReference.SUBJECT:
            if not self.in_modifier:
                raise RollItSyntaxError('Cannot refer to the subject outside of a modifier!')
            return self.subject
        if name == model.SpecialReference.ROOT:
            return self.root
        if name == model.SpecialReference.NONE:
            return None
        return self._scope[name]

    def __contains__(self, name):
        return name in self._scope

    def __setitem__(self, name, value):
        self._scope[name] = value

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return

    def roll(self, sides):
        """
        """
        return self._env.dice_tower.roll(sides)

    def evaluate(self, obj):
        """
        """
        if isinstance(obj, str):
            return self[obj]
        if isinstance(obj, (int, float)):
            return obj
        return self._evaluators[type(obj)](self, obj)

    def reduce(self, obj):
        """
        """
        if isinstance(obj, Reducable):
            return obj.reduce(self)
        # pylint: disable=unidiomatic-typecheck
        if type(obj) in self._reducers:
            return self._reducers[type(obj)](self, obj)
        raise CannotReduceError(obj)

    def access_obj(self, name, accessors):
        """
        """
        obj = self[name]
        for item in accessors:
            try:
                if obj is None or item not in obj:
                    raise NoneError()
                obj = obj[item]
            except TypeError:
                raise RollItTypeError()
        return obj


@ExecutionContext.evaluator(model.Reduce)
def _(context, obj):
    return context.reduce(obj)


@ExecutionContext.evaluator(model.Assignment)
def _(context, obj):
    if isinstance(obj.target, str):
        context[obj.target] = context.evaluate(obj.value)
    else:
        target = context.access_obj(obj.target.accessing, obj.target.accessors[:-1])
        target[obj.target.accessors[-1]] = context.evaluate(obj.value)


@ExecutionContext.evaluator(model.Access)
def _(context, obj):
    return context.access_obj(*obj)


@ExecutionContext.evaluator(model.Enlarge)
def _(context, obj):
    return Roll([context.evaluate(obj.value) for _ in range(obj.size)])


@ExecutionContext.evaluator(model.Dice)
@ExecutionContext.reducer(model.Dice)
def _(context, obj):
    number_of_dice = context.evaluate(obj.number_of_dice)
    sides = context.evaluate(obj.sides)
    return Roll([context.roll(sides) for _ in range(number_of_dice)])


@ExecutionContext.evaluator(model.Length)
def _(context, obj):
    try:
        return len(context.evaluate(obj.value))
    except TypeError:
        if obj is None:
            raise NoneError()
        raise RollItTypeError()


@ExecutionContext.evaluator(model.Negation)
def _(context, obj):
    return not context.evaluate(obj.value)


@ExecutionContext.evaluator(model.BinaryOp)
def _(context, obj):
    return _OPERATOR_MAP[obj.op](context.evaluate(obj.left), context.evaluate(obj.right))


@ExecutionContext.evaluator(model.CreateBag)
def _(context, obj):
    context[obj.value] = {}


@ExecutionContext.evaluator(model.UseIf)
def _(context, obj):
    if context.evaluate(obj.predicate):
        return context.evaluate(obj.use)
    return context.evaluate(obj.otherwise)


@ExecutionContext.evaluator(model.If)
def _(context, obj):
    if context.evaluate(obj.predicate):
        context.evaluate(obj.then)
    else:
        context.evaluate(obj.otherwise)


@ExecutionContext.evaluator(model.Modify)
def _(context, obj):
    raise NotImplementedError()


@ExecutionContext.evaluator(model.Load)
def _(context, obj):
    raise NotImplementedError()


@ExecutionContext.evaluator(model.ForEvery)
def _(context, obj):
    raise NotImplementedError()


@ExecutionContext.evaluator(model.ModifierDef)
def _(context, obj):
    raise NotImplementedError()


@ExecutionContext.evaluator(model.Restart)
def _(context, obj):
    raise NotImplementedError()


@ExecutionContext.evaluator(model.UntilDo)
def _(context, obj):
    raise NotImplementedError()
