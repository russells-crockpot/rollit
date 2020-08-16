"""
"""
import random  # nosec
from collections import namedtuple

__all__ = ['RollResults', 'Macro', 'macro', 'Modifier']


class RollResults:
    """
    """
    __slots__ = ('rolls', 'sides', '_value')

    def __init__(self, number_of_dice, sides):
        self.rolls = [random.randint(1, sides) for _ in range(number_of_dice)]  # nosec
        self.sides = sides
        self._value = None

    def __int__(self):
        return self.value

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

    @value.deleter
    def value(self):
        self._value = None

    @property
    def total(self):
        """
        """
        return sum(self.rolls)

    def __str__(self):
        rolls_str = ', '.join(str(r) for r in self.rolls)
        return (f'<{type(self).__qualname__} {len(self.rolls)}d{self.sides}: rolls=[{rolls_str}] '
                f'total={self.total}>')


Macro = namedtuple('Macro', ('name', 'run', 'help'))
""" """


# pylint: disable=redefined-builtin
def macro(name=None, *, help=None):
    """
    """

    def _decorator(func):
        if not name:
            name = func.__name__
        return Macro(name, func, help)

    return _decorator


class Modifier(namedtuple('_ModifierBase', ('help', 'run'))):
    """
    """

    def __call__(self, *args, roll):
        return self.run(*args, roll=roll)
