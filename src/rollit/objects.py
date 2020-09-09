"""Internal representations of rollit objects.
"""
from abc import ABCMeta, abstractmethod
from collections import namedtuple
from contextlib import suppress

from .ast import elements, ModelElement, ModelEnumElement, constants
from .exceptions import RollitTypeError, InvalidNameError
from .util import is_valid_iterable

__all__ = [
    'RollitNonErrorException',
    'LeaveException',
    'RestartException',
    'OopsException',
    'Dice',
    'Roll',
    'BagSpecialEntries',
    'Bag',
    'Modifier',
    'RollitBasedModifier',
    'NoSubject',
    'NoValue',
]


def __create_no_value():

    class _NoValueBase(tuple):
        __the_object = None

        def __new__(cls):
            if not cls.__the_object:
                cls.__the_object = super().__new__(cls)
            return cls.__the_object

        def __bool__(self):
            return False

        @staticmethod
        def __str__():
            return 'NoValue'

        @staticmethod
        def __repr__():
            return 'NoValue'

    return _NoValueBase()


NoValue = __create_no_value()
""" """
del __create_no_value


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


class RollitNonErrorException(BaseException):
    """An exception that is used as a sort of internal marker, but not as any sort of error.
    """


class LeaveException(RollitNonErrorException):
    """Used to indicate that a ``leave`` statement was issued.
    """
    __slots__ = ()
    __THE_EXCEPTION = None

    def __new__(cls):
        if not cls.__THE_EXCEPTION:
            cls.__THE_EXCEPTION = super().__new__(cls)
        return cls.__THE_EXCEPTION


class RestartException(RollitNonErrorException):
    """Used to indicate that a ``restart`` statement was issued.
    """
    __slots__ = ('location_specifier', 'name')

    #pylint: disable=super-init-not-called
    def __init__(self, location_specifier, name, *args):
        self.location_specifier = location_specifier
        self.name = name


class OopsException(RollitNonErrorException):
    """
    """
    __slots__ = ('value',)

    #pylint: disable=super-init-not-called
    def __init__(self, value):
        self.value = value


class OperatorImplementations:
    """
    """
    __slots__ = (
        *(op.left_python_name for op in elements.TwoSidedOperator),
        *(op.right_python_name for op in elements.TwoSidedOperator),
        *(op.python_name for op in elements.OneSidedOperator),
        *(op.python_name for op in elements.OverloadOnlyOperator),
    )

    def __init__(self, *, copy_from=None):
        if not copy_from:
            for attr in self.__slots__:
                setattr(self, attr, NotImplemented)
        else:
            for attr in self.__slots__:
                setattr(self, attr, getattr(copy_from, attr, NotImplemented))

    @staticmethod
    def _convert_key(key):
        if isinstance(key, elements.OverloadOperator):
            if key.side == elements.OperationSide.NA:
                return key.operator.python_name
            return getattr(key.operator, f'{key.side.name.lower()}_python_name')
        return key

    def __delattr__(self, name):
        setattr(self, name, NotImplemented)

    def __delitem__(self, key):
        setattr(self, self._convert_key(key), NotImplemented)

    def __getitem__(self, key):
        getattr(self, self._convert_key(key))

    def __setitem__(self, key, value):
        setattr(self, self._convert_key(key), value)

    def get_impl(self, operator, side=None):
        """
        """
        if isinstance(operator, elements.TwoSidedOperator):
            if not side:
                raise ValueError()
            key = getattr(operator, f'{side.name.lower()}_python_name')
        else:
            key = operator.python_name
        return getattr(self, key)

    def add_impl(self, operator, side=None):
        """
        """

        def _decorator(func):
            if isinstance(operator, elements.TwoSidedOperator):
                if not side:
                    raise ValueError()
                key = getattr(operator, f'{side.name.lower()}_python_name')
            else:
                key = operator.python_name
            setattr(self, key, func)
            return func

        return _decorator


class InternalObject(metaclass=ABCMeta):
    """
    """
    __slots__ = ('_op_impls',)

    default_ops_impl = None
    """ """

    def __init__(self):
        self._op_impls = OperatorImplementations(copy_from=self.default_ops_impl)

    def override_operator(self, key, override):
        """
        """
        self._op_impls[key] = override

    def __getattr__(self, name):
        if name in self._op_impls:
            return getattr(self._op_impls, name)
        raise AttributeError(name)

    def operate_on(self, context, operator, side=None, other=None):
        """
        """
        op_impl = self._op_impls.get_impl(operator, side=side)
        args = ()
        if not isinstance(operator, elements.OverloadOnlyOperator):
            args = (other,)
        if isinstance(op_impl, Modifier):
            with context.use_subject(self):
                op_impl.call(*args, context=context)
                return context.subject
        elif callable(op_impl):
            return op_impl(self, *args, context)
        return op_impl


class Dice(InternalObject):
    """
    """
    __slots__ = ('num_dice', 'sides')

    def __init__(self, num_dice, sides, *args, **kwargs):
        super().__init__()
        self.num_dice = num_dice
        self.sides = sides

    # pylint: disable=no-member, protected-access
    def __getitem__(self, key):
        if key in (elements.SpecialAccessor.LENGTH, elements.SpecialAccessor.LENGTH._value_):
            return self.num_dice
        if key in (elements.SpecialAccessor.PARENT, elements.SpecialAccessor.PARENT._value_):
            return self.sides
        raise RollitTypeError()

    # pylint: disable=no-member, protected-access
    def __setitem__(self, key, value):
        if key in (elements.SpecialAccessor.LENGTH, elements.SpecialAccessor.LENGTH._value_):
            self.num_dice = value
        elif key in (elements.SpecialAccessor.PARENT, elements.SpecialAccessor.PARENT._value_):
            self.sides = value
        else:
            raise RollitTypeError()

    def reduce(self, context):
        """
        """
        num_dice = context(self.num_dice)
        return Roll([context.roll(context(self.sides)) for _ in range(num_dice)])

    def __repr__(self):
        return str(self)

    def __str__(self):
        num_dice = self.num_dice
        if isinstance(num_dice, ModelElement):
            num_dice = f'({num_dice.codeinfo.text})'
        sides = self.sides
        if isinstance(sides, ModelElement):
            sides = f'({sides.codeinfo.text})'
        return f'{num_dice}d{sides}'


class Roll(InternalObject):
    """
    """
    default_ops_impl = OperatorImplementations()
    __slots__ = ('_items', '_value')

    def __init__(self, results=()):
        super().__init__()
        self._items = list(results)
        self._value = None

    def get_total(self, context):
        """
        """
        if not self._items:
            return 0
        running_total = self._items[0]
        for item in self._items[1:]:
            # pylint: disable=unexpected-keyword-arg
            running_total = context(
                elements.BinaryOp(
                    left=running_total,
                    op=elements.TwoSidedOperator.ADD,
                    right=item,
                    codeinfo=None,
                ))
        return running_total

    def get_value(self, context):
        """
        """
        if self._value is None:
            return self.get_total(context)
        return context(self._value)

    def __setattr__(self, name, value):
        if name == 'value':
            name = '_value'
        super().__setattr__(name, value)

    def __getitem__(self, key):
        if key == elements.SpecialAccessor.LENGTH:
            return len(self)
        if key in (elements.SpecialAccessor.VALUE, 0):
            return self.value
        if key == elements.SpecialAccessor.TOTAL:
            return self.total
        if key == elements.SpecialAccessor.EVERY:
            raise NotImplementedError()
        try:
            if key >= 1:
                key -= 1
            return self._items[key]
        except TypeError:
            raise RollitTypeError() from None

    def __setitem__(self, key, value):
        if key in (elements.SpecialAccessor.LENGTH, elements.SpecialAccessor.TOTAL):
            raise RuntimeError()
        if key in (elements.SpecialAccessor.VALUE, 0):
            self._value = value
        elif key == elements.SpecialAccessor.EVERY:
            raise NotImplementedError()
        else:
            try:
                if key >= 1:
                    key -= 1
                self._items[key] = value
            except TypeError:
                raise RollitTypeError() from None

    def __delitem__(self, key):
        if key in (elements.SpecialAccessor.LENGTH, elements.SpecialAccessor.TOTAL):
            raise RuntimeError()
        if key in (elements.SpecialAccessor.VALUE, 0):
            self._value = None
        if key == elements.SpecialAccessor.EVERY:
            self.clear()
        else:
            try:
                if key >= 1:
                    key -= 1
                del self._items[key]
            except TypeError:
                raise RollitTypeError() from None

    def __len__(self):
        return len(self._items)

    def __contains__(self, key):
        return key in self._items

    def __str__(self):
        return f'[{", ".join(str(r) for r in self._items)}]'

    def map_to(self, *args):
        """
        """
        raise NotImplementedError()

    def operate_on(self, context, operator, side=None, other=None):
        op_impl = super().operate_on(context, operator, side=side, other=other)
        if op_impl is NotImplemented:
            if isinstance(other, Roll) and operator not in (
                    elements.TwoSidedOperator.AMPERSAND,
                    elements.OneSidedOperator.HAS,
            ):
                other = other.get_value(context)
            value = self.get_value(context)
            if value is self:
                return NotImplemented
            if isinstance(value, InternalObject):
                return value.operate_on(context, operator, side=side, other=other)
            if operator.value in constants.OPERATOR_MAP:
                if side == elements.OperationSide.LEFT:
                    return constants.OPERATOR_MAP[operator.value](value, other)
                return constants.OPERATOR_MAP[operator.value](other, value)
        return op_impl


@Roll.default_ops_impl.add_impl(elements.OneSidedOperator.HAS)
def _(obj, context, other):
    return other in obj


@Roll.default_ops_impl.add_impl(elements.OverloadOnlyOperator.LENGTH)
def _(obj, context):
    return len(obj)


@Roll.default_ops_impl.add_impl(elements.OverloadOnlyOperator.REDUCE)
# pylint: disable=protected-access
def _(obj, context):
    value_reduced = False
    new_values = []
    for result in obj._items:
        if not isinstance(result, (int, float, str)):
            new_result = context.reduce(result)
            value_reduced = new_result is not result
            result = new_result
        new_values.append(result)
    if not value_reduced:
        return obj.get_value(context)
    roll = Roll(new_values)
    roll._value = obj._value
    return roll


# pylint: disable=protected-access
class BagSpecialEntries:
    """
    """
    __slots__ = ('_owner', '_context', 'parent', 'access', 'set', 'clear', 'create', 'destroy')

    def __init__(self, owner, context):
        super().__init__()
        self._owner = owner
        self._context = context
        self.parent = None
        self.access = None
        self.set = None
        self.clear = None
        self.create = None
        self.destroy = None

    @property
    def owner(self):
        """
        """
        return self._owner

    def _execute(self, entry_name, bag, *args, from_parent=False):
        with self._context.use_subject(bag):
            if from_parent:
                if self.parent:
                    entry = getattr(self.parent._special_entries, entry_name)
                else:
                    entry = None
            else:
                entry = getattr(self, entry_name)
            if entry:
                entry.call(*args, context=self._context)
                return self._context.subject
            if self.parent:
                method = getattr(self.parent._special_entries, f'on_{entry_name}')
                return method(*args, bag=bag)
            return NoValue

    def on_access(self, name, bag=None):
        """
        """
        bag = bag or self.owner
        rval = self._execute('access', bag, name)
        if rval in (NoSubject, NoValue):
            rval = bag.raw_get(name)
        if rval in (NoSubject, NoValue, bag):
            return None
        return rval

    def on_set(self, name, value, bag=None):
        """
        """
        bag = bag or self.owner
        rval = self._execute('set', bag, name, value)
        if rval is NoValue:
            return value
        return rval

    def on_clear(self, name, bag=None):
        """
        """
        bag = bag or self.owner
        rval = self._execute('clear', bag, name)
        if rval is NoValue:
            bag.raw_clear(name)

    def on_create(self, bag=None):
        """
        """
        bag = bag or self.owner
        if not bag.parent:
            return
        self._execute('create', bag, from_parent=True)

    def on_destroy(self, bag=None):
        """
        """
        bag = bag or self.owner
        self._execute('destroy', bag)

    def __delitem__(self, key):
        return setattr(self, key._name_.lower(), None)

    def __getitem__(self, key):
        try:
            return getattr(self, key._name_.lower())
        except AttributeError:
            raise KeyError(key)

    # pylint: disable=no-member
    def __setitem__(self, key, value):
        if key in (elements.SpecialEntry.PARENT, elements.SpecialEntry.PARENT._value_):
            self.parent = value
        elif key in (elements.SpecialEntry.CREATE, elements.SpecialEntry.CREATE._value_):
            self.create = value
        elif key in (elements.SpecialEntry.ACCESS, elements.SpecialEntry.ACCESS._value_):
            self.access = value
        elif key in (elements.SpecialEntry.CLEAR, elements.SpecialEntry.CLEAR._value_):
            self.clear = value
        elif key in (elements.SpecialEntry.SET, elements.SpecialEntry.SET._value_):
            self.set = value
        else:
            raise KeyError(key)


class Bag(InternalObject):
    """
    """
    default_ops_impl = OperatorImplementations()
    __slots__ = ('_entries', '_context', '_special_entries')

    def __init__(self, context):
        super().__init__()
        self._context = context
        self._special_entries = BagSpecialEntries(self, self._context)
        self._entries = {}

    def keys(self):
        """
        """
        return self._entries.keys

    def __repr__(self):
        return str(self._entries)

    def __str__(self):
        return str(self._entries)

    @property
    def parent(self):
        """
        """
        return self._special_entries.parent

    # pylint: disable=protected-access
    def load(self, bag):
        """
        """
        if not bag:
            return
        if isinstance(bag, Bag):
            bag = bag._entries
        self._entries.update(bag)

    # pylint: disable=no-member,protected-access
    def __getitem__(self, key):
        if key in (elements.SpecialAccessor.LENGTH, elements.SpecialAccessor.LENGTH._value_):
            return len(self)
        if isinstance(key, elements.SpecialEntry):
            return self._special_entries[key]
        rval = self._special_entries.on_access(key)
        if rval in (NoValue, NoSubject):
            raise InvalidNameError(key)
        return rval

    def __setitem__(self, key, value):
        if key in (elements.SpecialAccessor.LENGTH, elements.SpecialAccessor.LENGTH._value_):
            raise RollitTypeError()
        if isinstance(key, elements.SpecialEntry):
            self._special_entries[key] = value
        else:
            rval = self._special_entries.on_set(key, value)
            if rval is not self:
                self._entries[key] = rval

    def __delitem__(self, key):
        if key in (elements.SpecialAccessor.LENGTH, elements.SpecialAccessor.LENGTH._value_):
            raise RollitTypeError()
        if isinstance(key, elements.SpecialEntry):
            del self._special_entries[key]
        else:
            self._special_entries.on_clear(key)

    def raw_clear(self, key):
        """
        """
        if isinstance(key, elements.SpecialEntry):
            del self._special_entries[key]
        else:
            del self._entries[key]

    def raw_set(self, key, value):
        """
        """
        if isinstance(key, elements.SpecialEntry):
            self._special_entries[key] = value
        else:
            self._entries[key] = value

    def raw_get(self, key):
        """
        """
        if isinstance(key, elements.SpecialEntry):
            return self._special_entries[key]
        if key in self._entries:
            return self._entries[key]
        if self._special_entries.parent:
            return self.parent.raw_get(key)
        raise InvalidNameError(key)

    def __len__(self):
        return len(self._entries)

    def __contains__(self, key):
        return key in self._entries or (self.parent and key in self.parent)

    def __iter__(self):
        return iter(Roll(*item) for item in self._entries.items())

    def __reversed__(self):
        return reversed(Roll(*item) for item in self._entries.items())

    def __bool__(self):
        return True


class Modifier(metaclass=ABCMeta):
    """
    """
    __slots__ = ()

    def call(self, *args, context):
        """
        """
        scope = context.scope
        with context.new_scope(scope, isolate=True) as scope:
            context.scope.error = scope.error
            context.scope.subject = scope.subject
            self.modify(*args, context=context)
            scope.subject = context.scope.subject

    @abstractmethod
    def modify(self, *args, context):
        """
        """

    @property
    @abstractmethod
    def display_string(self):
        """
        """

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.display_string


InternalObject.register(Modifier)


class RollitBasedModifier(
        namedtuple('_RollitBasedModifierBase', ('parameters', 'body', 'scope', 'display_string')),
        Modifier):
    """
    """

    def __new__(cls, modifier_def, scope):
        target_name = modifier_def.target
        if isinstance(target_name, elements.Access):
            target_name = target_name.accessors[-1]
        if target_name in (None, elements.SpecialReference.NONE):
            display_string = '[- lambda -]'
        elif isinstance(target_name, ModelEnumElement):
            # pylint: disable=protected-access
            display_string = f'[- modifier: <{target_name._value_}> -]'
        else:
            display_string = f'[- modifier: {target_name.codeinfo.text} -]'
        body = modifier_def.definition
        if not is_valid_iterable(body):
            body = (body,)
        return super().__new__(cls,
                               display_string=display_string,
                               parameters=modifier_def.parameters,
                               body=body,
                               scope=scope)

    def modify(self, *args, context):
        if args is not None:
            context.scope.load(dict(zip(self.parameters, args)))
        context.scope.load(self.scope)
        with suppress(LeaveException):
            for statement in self.body:
                context(statement)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.display_string
