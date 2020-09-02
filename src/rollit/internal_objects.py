"""
"""
from abc import ABCMeta, abstractmethod
from collections import namedtuple
from contextlib import suppress

from .ast import elements, is_valid_iterable
from .exceptions import RollitTypeError
from .execution.base import NoSubject

__all__ = []


class RollitNonErrorException(BaseException):
    """
    """


class LeaveException(RollitNonErrorException):
    """
    """
    __THE_EXCEPTION = None

    def __new__(cls):
        if not cls.__THE_EXCEPTION:
            cls.__THE_EXCEPTION = object.__new__(cls)
        return cls.__THE_EXCEPTION


class RestartException(RollitNonErrorException):
    """
    """
    location_specifier = name = None

    #pylint: disable=super-init-not-called
    def __init__(self, restart_obj):
        self.location_specifier, self.name = restart_obj


class OopsException(RollitNonErrorException):
    """
    """

    #pylint: disable=super-init-not-called
    def __init__(self, value):
        self.value = value


class Roll(list):
    """
    """

    def __init__(self, results):
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


class Bag(dict):
    """
    """


class Modifier(metaclass=ABCMeta):
    """
    """

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
        if modifier_def.target in (None, elements.SpecialReference.NONE):
            display_string = '[-lambda-]'
        else:
            display_string = f'[-modifier: {modifier_def.target.codeinfo.text}-]'
        body = modifier_def.definition
        if not is_valid_iterable(body):
            body = (body,)
        return super().__new__(cls,
                               display_string=display_string,
                               parameters=modifier_def.parameters,
                               body=body,
                               scope=scope)

    def modify(self, *args, context):
        scope = context.scope
        with context.new_scope(scope, isolate=True) as call_scope:
            call_scope.load(self.scope)
            call_scope.subject = scope.subject
            call_scope.error = scope.error
            if args is not None:
                call_scope.load(dict(zip(self.parameters, args)))
            with suppress(LeaveException):
                for statement in self.body:
                    context(statement)
            scope.subject = call_scope.subject

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.display_string
