"""
"""
from abc import ABCMeta, abstractmethod

from .ast import elements
from .exceptions import RollitTypeError

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
    def modify(self, *args, scope, context):
        """
        """


class PythonBasedModifier(Modifier):
    """
    """
    __slots__ = ('func',)

    def __init__(self, func):
        self.func = func

    def modify(self, *args, subject, context):
        val = self.func(*args, subject=subject, context=context)
        if val is not None:
            context['?'] = val
