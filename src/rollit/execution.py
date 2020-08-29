#pylint: disable=too-many-function-args
"""
"""
import inspect
import sys
from collections import ChainMap
from contextlib import suppress

from . import grammar
from .ast import actions, constants, elements, flatten_tuple, is_valid_iterable, \
        ModelElement, SingleValueElement
from .exceptions import InvalidNameError, RollItSyntaxError, NoSuchLoopError, RollItTypeError, \
        NoneError, CannotReduceError, RollitIndexError, RollitReferenceError
from .internal_objects import Roll, OopsException
from .towers import DefaultTower

if sys.version_info.minor >= 8:
    from functools import cached_property
else:
    cached_property = property

__all__ = ['ExecutionEnvironment', 'ExecutionContext', 'NoSubject', 'Scope']


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

    #TODO protect parent scope?
    def __delitem__(self, name):
        if self._parent and not self._isolated and name in self._parent:
            del self._parent[name]
        del self._variables[name]

    def variable_names(self):
        """
        """
        return tuple(self._variables.keys())

    def loop_names(self):
        """
        """
        return tuple(self._loops.keys())


_DEFAULT_SEARCH_PATH = ('.',)


class ExecutionEnvironment:
    """
    """

    def __init__(self,
                 search_path=_DEFAULT_SEARCH_PATH,
                 *,
                 dice_tower=DefaultTower,
                 parser_options=None):
        if inspect.isclass(dice_tower):
            dice_tower = dice_tower()
        self.dice_tower = dice_tower
        self._context = ExecutionContext(env=self)
        self._search_path = search_path

    def run(self, script):
        """
        """
        script_model = grammar.parse(script, actions=actions)
        if not isinstance(script_model, ModelElement) \
                and isinstance(script_model, (tuple, list)) and len(script_model) == 1:
            script_model = script_model[0]
        if not isinstance(script_model, ModelElement) \
                and isinstance(script_model, (tuple, list)):
            return tuple(self._context(item) for item in flatten_tuple(script_model))
        return self._context(script_model)

    def current_variable_names(self):
        """
        """
        # pylint: disable=protected-access
        self._context._scope.variable_names()

    def current_loop_names(self):
        """
        """
        # pylint: disable=protected-access
        self._context._scope.loop_names()


def __create_no_subject():

    class _NoSubjectBase(tuple):
        __the_object = None

        def __new__(cls):
            if not cls.__the_object:
                cls.__the_object = super().__new__(cls)
            return cls.__the_object

        def __bool__(self):
            return False

        @staticmethod
        def __str__():
            return 'NoSubject'

        @staticmethod
        def __repr__():
            return 'NoSubject'

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

    def __init__(self, *, subject=NoSubject, loop=None, env=None, error=None, _parent=None):
        self._parent = _parent
        self._env = env or self._parent._env
        self._loop = loop
        self.__subject = subject
        if not self._parent:
            self._scope = Scope()
        #CONSIDER scopes and modifier calls and defs
        elif (self.in_modifier and not self._parent.in_modifier) or error:
            self._parent = self._scope = Scope(self._parent.root, isolate=True)
            self._parent = self._parent.root
        else:
            self._scope = Scope(self._parent._scope)
        self._error = error

    @classmethod
    def reducer(cls, obj_type):
        """
        """

        def _decorator(func):
            cls._reducers[obj_type] = func
            return func

        return _decorator

    @classmethod
    def evaluator(cls, obj_type, *, evaluate_children=False):
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
    def current_error(self):
        """
        """
        if self._parent and not self._error:
            return self._parent.current_error
        return self._error

    @cached_property
    def root(self):
        """
        """
        if self._parent:
            return self._parent.root
        return self

    def create_child(self, subject=None, loop=None, error=None):
        """
        """
        return type(self)(subject=subject, loop=loop, error=error, _parent=self)

    def get_loop(self, name):
        """
        """
        if name == elements.SpecialReference.NONE:
            return self.current_loop
        if name == elements.SpecialReference.ROOT:
            return self.root_loop
        return self._scope.get_loop(name)

    def __contains__(self, name):
        return name in self._scope

    def __getitem__(self, name):
        if name == elements.SpecialReference.SUBJECT:
            if not self.in_modifier:
                raise RollItSyntaxError('Cannot refer to the subject outside of a modifier!')
            return self.subject
        if name == elements.SpecialReference.ROOT:
            return self.root
        if name == elements.SpecialReference.ERROR:
            return self.current_error
        if name == elements.SpecialReference.NONE:
            return None
        return self._scope[name]

    def __setitem__(self, name, value):
        self._scope[name] = value

    def __delitem__(self, name):
        del self._scope[name]

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return

    def roll(self, sides):
        """
        """
        return self._env.dice_tower.roll(sides)

    def __call__(self, obj):
        return self.evaluate(obj)

    def evaluate(self, obj):
        """
        """
        if isinstance(obj, (int, float)) or obj is None:
            return obj
        if isinstance(obj, (str, elements.SpecialReference)):
            return self[obj]
        if isinstance(obj, elements.StringLiteral):
            return ''.join(obj)
        return self._evaluators[type(obj)](self, obj)

    def reduce(self, obj):
        """
        """
        if isinstance(obj, (int, float, str)) or obj is None:
            return obj
        # pylint: disable=unidiomatic-typecheck
        if type(obj) in self._reducers:
            return self._reducers[type(obj)](self, obj)
        raise CannotReduceError(obj)

    def full_reduce(self, obj):
        """
        """
        seen = []
        seen.append(self.reduce(obj))
        while seen[-1] is not None and not isinstance(seen[-1], (str, int, float)):
            reduced_value = self.reduce(seen[-1])
            if reduced_value in seen:
                raise RuntimeError()
            seen.append(reduced_value)
        return seen[-1]

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

    def evaluate_children(self, obj):
        """Evaluates all of the children of a :class:`~rollit.ast.ModelElement` and returns an
        object that is exactly the same, but each attribute has been evaluated.

        .. warning::

            If the element is a :class:`~rollit.ast.SingleValueElement`, then that element's
            evaluated value is returned instead of a copy of the element itself.
        """
        if isinstance(obj, (int, float)) or obj is None:
            return obj
        if is_valid_iterable(obj):
            return type(obj)(self.evaluate_children(o) for o in obj)
        if not isinstance(obj, ModelElement):
            return self.evaluate(obj)
        if isinstance(obj, SingleValueElement):
            return self.evaluate(obj.value)
        return type(obj)(**{
            k: self.evaluate(v) for k, v in obj._asdict().items() if k != 'codeinfo'
        },
                         codeinfo=obj.codeinfo)

    #pylint: disable = too-complex
    def _access(self, accessing, accessor):
        if accessing in (None, elements.SpecialReference.NONE):
            raise NoneError()
        try:
            if isinstance(accessor, elements.SpecialAccessor):
                if accessor == elements.SpecialAccessor.LENGTH:
                    return len(accessing)
                if accessor == elements.SpecialAccessor.VALUE:
                    return accessing.value
                if accessor == elements.SpecialAccessor.TOTAL:
                    return accessing.total
                raise NotImplementedError()
            if isinstance(accessor, (str, int)):
                return accessing[accessor]
            if isinstance(accessor, elements.Reduce):
                return self.access(accessing, self.reduce(accessor))
            return accessing[accessor]
        except TypeError:
            raise RollItTypeError()
        except (AttributeError, KeyError):
            raise RollitReferenceError()
        except IndexError:
            raise RollitIndexError()

    def access(self, accessing, *accessors):
        """
        """
        if not accessors:
            return accessing
        for accessor in accessors:
            accessing = self._access(accessing, accessor)
        return accessing


@ExecutionContext.evaluator(elements.Reduce)
def _(context, obj):
    return context.reduce(context(obj.value))


@ExecutionContext.evaluator(elements.Assignment)
def _(context, obj):
    if isinstance(obj.target, str):
        context[obj.target] = context(obj.value)
    else:
        target = context.access_obj(obj.target.accessing, obj.target.accessors[:-1])
        target[obj.target.accessors[-1]] = context(obj.value)


@ExecutionContext.evaluator(elements.Access)
def _(context, obj):
    if isinstance(obj.accessing, str):
        current_item = context[obj.accessing]
    else:
        current_item = context(obj.accessing)
    return context.access(current_item, *obj.accessors)


@ExecutionContext.evaluator(elements.Enlarge)
def _(context, obj):
    return Roll(context(obj.value) for _ in range(context(obj.size)))


@ExecutionContext.evaluator(elements.Dice)
def _(context, obj):
    return obj


@ExecutionContext.evaluator(elements.Negation)
def _(context, obj):
    return not context(obj.value)


@ExecutionContext.evaluator(elements.BinaryOp)
def _(context, obj):
    left = context(obj.left)
    right = context(obj.right)
    #FIXME handle string concatination and other operators
    if obj.op in constants.MATH_OPERATORS:
        left = context.full_reduce(left)
        right = context.full_reduce(right)
    return constants.OPERATOR_MAP[obj.op](left, right)


@ExecutionContext.evaluator(elements.NewBag)
def _(context, obj):
    return {}


# Because these objects are predicated, we can just have their children be evaluated
@ExecutionContext.evaluator(elements.ButIf)
@ExecutionContext.evaluator(elements.UseIf)
@ExecutionContext.evaluator(elements.IfThen)
def _(context, obj):
    return context.evaluate_children(obj)


@ExecutionContext.evaluator(elements.ClearValue)
def _(context, obj):
    to_clear = obj.value
    if isinstance(to_clear, elements.Access):
        #TODO
        base = context(
            elements.Access(to_clear.accessing, to_clear.accessors[:-1], codeinfo=obj.codeinfo))
        last = context.get_accessor_value(to_clear.accessors[-1])
        with suppress(LookupError):
            try:
                del base[last]
            except TypeError:
                raise RollItTypeError()
    else:
        del context[to_clear]


@ExecutionContext.evaluator(elements.Oops)
def _(context, obj):
    raise OopsException(context(obj.value))


@ExecutionContext.evaluator(elements.Attempt)
def _(context, obj):
    raise NotImplementedError()


@ExecutionContext.evaluator(elements.Leave)
def _(context, obj):
    raise NotImplementedError()


@ExecutionContext.evaluator(elements.Modify)
def _(context, obj):
    raise NotImplementedError()


@ExecutionContext.evaluator(elements.Load)
def _(context, obj):
    raise NotImplementedError()


@ExecutionContext.evaluator(elements.ForEvery)
def _(context, obj):
    raise NotImplementedError()


@ExecutionContext.evaluator(elements.ModifierDef)
def _(context, obj):
    raise NotImplementedError()


@ExecutionContext.evaluator(elements.Restart)
def _(context, obj):
    raise NotImplementedError()


@ExecutionContext.evaluator(elements.UntilDo)
def _(context, obj):
    raise NotImplementedError()


@ExecutionContext.reducer(Roll)
def _(context, obj):
    value_reduced = False
    new_values = []
    for result in obj:
        if not isinstance(result, (int, float)):
            result = context.reduce(result)
            value_reduced = True
        new_values.append(result)
    if not value_reduced:
        return obj.value
    roll = Roll(new_values)
    # pylint: disable=protected-access
    roll._value = obj._value
    return roll


@ExecutionContext.reducer(elements.Dice)
def _(context, obj):
    number_of_dice = context(obj.number_of_dice)
    return Roll([context.roll(context(obj.sides)) for _ in range(number_of_dice)])
