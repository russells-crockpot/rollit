"""
"""
from abc import ABCMeta, abstractmethod
from collections import namedtuple
from contextlib import suppress

from ..ast import elements, ModelElement, ModelEnumElement
from ..exceptions import RollitTypeError, InvalidNameError
from .base import NoSubject, NoValue
from ..util import is_valid_iterable

__all__ = []


class RollitNonErrorException(BaseException):
    """
    """


class LeaveException(RollitNonErrorException):
    """
    """
    __slots__ = ()
    __THE_EXCEPTION = None

    def __new__(cls):
        if not cls.__THE_EXCEPTION:
            cls.__THE_EXCEPTION = super().__new__(cls)
        return cls.__THE_EXCEPTION


class RestartException(RollitNonErrorException):
    """
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


class ObjectPlaceholder(metaclass=ABCMeta):
    """
    """
    __slots__ = ('_preloaders', '_postloaders')

    def __init__(self):
        self._preloaders = []
        self._postloaders = []

    #TODO handle modifiers
    def _run_load_op(self, context, op, obj):
        if not op:
            return
        if is_valid_iterable(op):
            for item in op:
                self._run_load_op(context, item, obj)
        elif isinstance(op, ModelElement):
            context(op)
        elif callable(op):
            op(obj, context)
        else:
            raise TypeError()

    def resolve(self, context):
        """
        """
        for op in self._preloaders:
            self._run_load_op(context, op, self)
        obj = self.get_object(context)
        for op in self._postloaders:
            self._run_load_op(context, op, obj)
        return obj

    @abstractmethod
    def get_object(self, context):
        """
        """

    def preloader(self, func):
        """
        """
        self._preloaders.append(func)
        return func

    def postloader(self, func):
        """
        """
        self._postloaders.append(func)
        return func


class Dice:
    """
    """
    __slots__ = ('num_dice', 'sides')

    def __init__(self, num_dice, sides, *args, **kwargs):
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


class Roll(list):
    """
    """

    def __init__(self, results=()):
        super().__init__(results)
        self._value = None

    @property
    def total(self):
        """
        """
        return sum(int(i) for i in self)

    @property
    def value(self):
        """
        """
        if self._value is None:
            return self.total
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def reduce(self, context):
        """
        """
        value_reduced = False
        new_values = []
        for result in self:
            if not isinstance(result, (int, float)):
                result = context.reduce(result)
                value_reduced = True
            new_values.append(result)
        if not value_reduced:
            return self.value
        roll = Roll(new_values)
        # pylint: disable=protected-access
        roll._value = self._value
        return roll

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
            return super().__getitem__(key)
        except TypeError:
            raise RollitTypeError() from None

    def __setitem__(self, key, value):
        if key in (elements.SpecialAccessor.LENGTH, elements.SpecialAccessor.TOTAL):
            raise RuntimeError()
        if key in (elements.SpecialAccessor.VALUE, 0):
            self.value = value
        elif key == elements.SpecialAccessor.EVERY:
            raise NotImplementedError()
        else:
            try:
                if key >= 1:
                    key -= 1
                super().__setitem__(key, value)
            except TypeError:
                raise RollitTypeError() from None

    def __delitem__(self, key):
        if key in (elements.SpecialAccessor.LENGTH, elements.SpecialAccessor.TOTAL):
            raise RuntimeError()
        if key in (elements.SpecialAccessor.VALUE, 0):
            self.value = None
        if key == elements.SpecialAccessor.EVERY:
            self.clear()
        else:
            try:
                if key >= 1:
                    key -= 1
                super().__delitem__(key)
            except TypeError:
                raise RollitTypeError() from None

    def __float__(self):
        return float(self.value)

    def __int__(self):
        return int(self.value)

    def __str__(self):
        return f'[{", ".join(str(r) for r in self)}]'

    def map_to(self, *args):
        """
        """
        raise NotImplementedError()

    def __add__(self, other):
        return self.value + other

    def __sub__(self, other):
        return self.value - other

    def __mul__(self, other):
        return self.value * other

    def __truediv__(self, other):
        return self.value / other

    def __floordiv__(self, other):
        return self.value // other

    def __mod__(self, other):
        return self.value % other

    def __radd__(self, other):
        return other + self.value

    def __rsub__(self, other):
        return other - self.value

    def __rmul__(self, other):
        return other * self.value

    def __rtruediv__(self, other):
        return other / self.value

    def __rfloordiv__(self, other):
        return other // self.value

    def __rmod__(self, other):
        return other % self.value


# pylint: disable=protected-access
class BagSpecialEntries:
    """
    """
    __slots__ = ('_owner', '_context', 'parent', 'access', 'set', 'clear', 'create', 'destroy')

    def __init__(self, owner, context):
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


class Bag:
    """
    """
    __slots__ = ('_entries', '_context', '_special_entries')

    def __init__(self, context):
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


class BagPlaceholder(ObjectPlaceholder):
    """
    """
    __slots__ = ('_entries', '_raw')

    def __init__(self, entries, raw=False):
        super().__init__()
        self._entries = entries
        self._raw = raw

    def get_object(self, context):
        bag = Bag(context)
        for k, v in self._entries.items():
            if self._raw is True:
                bag.raw_set(k, v)
            else:
                bag[k] = v
        if isinstance(self._raw, dict):
            for k, v in self._raw.items():
                bag.raw_set(k, v)
        return bag


class Modifier(metaclass=ABCMeta):
    """
    """

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


class PythonBasedModifier(Modifier):
    """
    """
    __slots__ = (
        '_display_string',
        'func',
    )

    def __init__(self, func):
        self.func = func
        self._display_string = f'[-built-in modifier: {self.func.__name__.lstrip("_")}-]'

    def modify(self, *args, context):
        val = self.func(*args, subject=context.scope.subject, context=context)
        if val not in (None, NoSubject):
            context.scope.subject = val

    @property
    def display_string(self):
        return self._display_string

    @display_string.setter
    def display_string(self, value):
        self._display_string = value


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
