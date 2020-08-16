"""
"""
import random  # nosec
from collections import namedtuple

from lark import Token

__all__ = [
    'ModifierCall',
    'DiceRoll',
    'RollResults',
    'Macro',
    'macro',
    'Modifier',
]

ModifierCall = namedtuple('ModifierCall', ('name', 'modifier', 'args'))
""" """


class DiceRoll(namedtuple('_DiceRollBase', ('number_of_dice', 'sides', 'modifiers'))):
    """An imutable representation of a dice roll definition.

    .. attribute:: number_of_dice

        The number of dice in this roll.

    .. attribute:: sides

        How many sides the dice in this roll have.

    .. attribute:: modifiers

        Any modifier calls for this dice roll.
    """

    def __new__(cls, number_of_dice, sides, modifiers=()):
        if isinstance(number_of_dice, Token):
            number_of_dice = int(number_of_dice.value)
        if isinstance(sides, Token):
            sides = int(sides.value)
        if not isinstance(modifiers, tuple):
            modifiers = tuple(modifiers)
        return super().__new__(cls, number_of_dice, sides, modifiers)

    # pylint: disable=missing-raises-doc
    def roll(self):
        """Rolls the dice represented by this object.

        :returns: The roll results.
        :rtype: RollResults
        """
        number_of_dice = self.number_of_dice
        if isinstance(number_of_dice, DiceRoll):
            number_of_dice = number_of_dice.roll().total
        sides = self.sides
        if isinstance(sides, DiceRoll):
            sides = sides.roll().total
        results = RollResults(number_of_dice, sides)
        for _, modifier, args in self.modifiers:
            new_args = []
            for arg in args:
                if isinstance(arg, DiceRoll):
                    arg = arg.roll()
                if isinstance(arg, RollResults):
                    arg = arg.total
            modified = modifier(*new_args, roll=results)
            if isinstance(modified, (set, tuple, list)):
                results.rolls = modified
            elif isinstance(modified, (int, float)):
                results.value = modified
            elif isinstance(modified, RollResults):
                results = modified
            else:
                raise TypeError(f'Invalid modifier return type: {type(modified).__qualname__}')
        return results

    def __str__(self):
        mod_parts = []
        for name, _, args in self.modifiers:
            if not mod_parts:
                mod_parts.append('')
            mod_parts.append(f'{name}({", ".join(str(a) for a in args)})')
        return (f'<{type(self).__qualname__} {self.number_of_dice}d{self.sides}'
                f'{":".join(mod_parts)}>')


class RollResults:
    """The results of a roll.

    .. attribute:: rolls

        A list containing the results of each individual roll.

    """
    __slots__ = ('rolls', '_value')

    def __init__(self, number_of_dice, sides):
        self.rolls = [random.randint(1, sides) for _ in range(number_of_dice)]  # nosec
        self._value = None

    def __int__(self):
        return self.value

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
