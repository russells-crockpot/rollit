"""
"""
import random  # nosec
from collections import namedtuple

__all__ = [
    'macro',
    'Macro',
    'Modifier',
    'RollResults',
]

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


class RollResults:
    """The results of a roll.

    .. attribute:: rolls

        A list containing the results of each individual roll.

    """
    __slots__ = ('rolls', '_value')

    def __init__(self, number_of_dice, sides):
        self.rolls = [random.randint(1, sides) for _ in range(number_of_dice)]  # nosec
        self._value = None

    @property
    def value(self):
        """The value of the roll. By default, this is simply the :attr:`~.total`, but it can be
        replaced with a different value (useful for thins like fudging rolls).
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
        """The total value of all of the :attr:`~.rolls` added together.
        """
        return sum(self.rolls)

    def __str__(self):
        rolls_str = ', '.join(str(r) for r in self.rolls)
        return f'<{type(self).__qualname__} rolls=[{rolls_str}] total={self.total}>'
