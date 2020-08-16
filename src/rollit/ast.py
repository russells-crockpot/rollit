"""
"""
import enum
import operator
from abc import ABCMeta, abstractmethod
from collections import namedtuple
from contextlib import suppress

from .elements import RollResults
from ._parser import Token

__all__ = [
    'ModifierCall',
    'DiceRoll',
]


class Resolvable(metaclass=ABCMeta):
    """
    """
    __slots__ = ()

    @staticmethod
    def value_for(item, context):
        """
        """
        if isinstance(item, Token):
            with suppress(ValueError):
                return int(item.value)
            return item.value
        if isinstance(item, Resolvable):
            return item.resolve(context)
        return item

    @abstractmethod
    def resolve(self, context):
        """
        """


class DefinitionType(enum.Enum):
    """
    """
    ALIAS = 'alias'
    """ """
    SUBSTITUTION = 'substitution'
    """ """
    MODIFIER = 'modifier'
    """ """


class Definition(namedtuple('_DefinitionBase', ('name', 'value', 'type')), Resolvable):
    """
    """

    def resolve(self, context):
        value = self.value_for(self.value, context)
        # pylint: disable=protected-access
        add_func = getattr(context, f'add_{self.type._value_}')
        add_func(self.name, value)


class MacroCall(namedtuple('_MacroCallBase', ('name', 'args')), Resolvable):
    """
    """

    def resolve(self, context):
        return context.get_macro(self.name)


class ModifierCall(namedtuple('_ModifierCallBase', ('name', 'args')), Resolvable):
    """
    """

    def resolve(self, context):
        return context.get_modifier(self.name)


class Substitution(namedtuple('_SubstitutionBase', ('name',)), Resolvable):
    """
    """

    def resolve(self, context):
        return context.get_substitution(self.name)


class DialectSwitch(namedtuple('_DialectSwitchBase', ('name', 'parent')), Resolvable):
    """
    """

    @staticmethod
    def _get_dialect(name, dialect):
        if name == '^':
            if not dialect.parent:
                raise Exception()
            return dialect.parent
        if name == '~':
            return dialect.root
        return None

    def resolve(self, context):
        pass


class Repeat(namedtuple('_RepeatBase', ('statement', 'times')), Resolvable):
    """
    """

    def resolve(self, context):
        return tuple(
            self.value_for(self.statement, context)
            for _ in range(self.value_for(self.times, context)))


class Math(namedtuple('_MathBase', ('left', 'op', 'right')), Resolvable):
    """
    """

    _OP_MAP = {
        'STAR': operator.mul,
        'PLUS': operator.add,
        'MINUS': operator.sub,
        'SLASH': operator.floordiv,  #CONSIDER addind way to get remainder, etcetera
    }

    def resolve(self, context):
        return self._OP_MAP[self.op](self.value_for(self.left, context),
                                     self.value_for(self.right, context))


class DiceRoll(namedtuple('_DiceRollBase', ('number_of_dice', 'sides', 'modifiers')), Resolvable):
    """An immutable representation of a dice roll definition.

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

    def resolve(self, context):
        return self.roll(context)

    # pylint: disable=missing-raises-doc
    def roll(self, context):
        """Rolls the dice represented by this object.

        :param Dialect context: The context to use.

        :returns: The roll results.
        :rtype: RollResults
        """
        number_of_dice = self.value_for(self.number_of_dice, context)
        if isinstance(number_of_dice, RollResults):
            number_of_dice = number_of_dice.value
        sides = self.value_for(self.sides, context)
        if isinstance(sides, RollResults):
            sides = sides.value
        results = RollResults(number_of_dice, sides)
        for name, args in self.modifiers:
            modifier = context.get_modifier(name)
            new_args = []
            for arg in args:
                arg = self.value_for(arg, context)
                if isinstance(arg, RollResults):
                    arg = arg.value
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
        for name, args in self.modifiers:
            if not mod_parts:
                mod_parts.append('')
            mod_parts.append(f'{name}({", ".join(str(a) for a in args)})')
        return (f'<{type(self).__qualname__} {self.number_of_dice}d{self.sides}'
                f'{":".join(mod_parts)}>')
