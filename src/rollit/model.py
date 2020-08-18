"""
"""
import operator
from abc import ABCMeta, abstractmethod
from collections import namedtuple

from .elements import RollResults

__all__ = [
    'Resolvable',
    'MacroCall',
    'ModifierCall',
    'Assignment',
    'Reference',
    'Use',
    'Math',
    'Dice',
    'Modify',
    'Pack',
    'Freeze',
    'Length',
]


class Resolvable(metaclass=ABCMeta):
    """
    """
    __slots__ = ()

    @abstractmethod
    def resolve(self, context):
        """
        """


class MacroCall(namedtuple('_MacroCallBase', ('name', 'args')), Resolvable):
    """
    """

    def resolve(self, context):
        context.current_dialect.get_macro(self.name)(context[a] for a in self.args)


class ModifierCall(namedtuple('_ModifierCallBase', ('name', 'args')), Resolvable):
    """
    """

    def resolve(self, context):
        # args = (context[a] for a in self.args)
        # return context.current_dialect.get_modifier(self.name)
        raise NotImplementedError()


class Reference(namedtuple('_ReferenceBase', ('name',)), Resolvable):
    """
    """

    def resolve(self, context):
        return context.dialect.get_variable(self.name)


class Assignment(namedtuple('_AssignmentBase', ('name', 'value')), Resolvable):
    """
    """

    def resolve(self, context):
        context.dialect.add_variable(self.name, context[self.value])


class Use(namedtuple('_UseBase', ('name', 'parent')), Resolvable):
    """
    """

    def resolve(self, context):
        context.current_dialect = context.get_or_create_dialect(self.name, self.parent)


class Pack(namedtuple('_PackBase', ('times', 'packed')), Resolvable):
    """
    """

    def resolve(self, context):
        return RollResults([context[self.packed] for _ in range(context[self.times])])


class Math(namedtuple('_MathBase', ('left', 'op', 'right')), Resolvable):
    """
    """

    _OP_MAP = {
        '*': operator.mul,
        '+': operator.add,
        '-': operator.sub,
        '/': operator.truediv,
        '//': operator.floordiv,
    }

    def __new__(cls, left, op, right):
        if isinstance(op, str):
            op = cls._OP_MAP[op]
        return super().__new__(cls, left, op, right)

    def resolve(self, context):
        return self.op(context[self.left], context[self.right])

    def __str__(self):
        return f'<{type(self).__qualname__}: {self.left} {self.op} {self.right}>'


class Modify(namedtuple('_ModifyBase', ('modifying', 'modifiers')), Resolvable):
    """
    """

    def resolve(self, context):
        roll_results = context[self.modifying]
        for modifier_call in self.modifiers:
            modifier, args = context[modifier_call]
            new_args = []
            for arg in args:
                arg = context[arg]
                if isinstance(arg, RollResults):
                    arg = arg.value
            modified = modifier(*new_args, roll=roll_results)
            if isinstance(modified, (set, tuple, list)):
                roll_results.rolls = modified
            elif isinstance(modified, (int, float)):
                roll_results.value = modified
            elif isinstance(modified, RollResults):
                roll_results = modified
            else:
                raise TypeError(f'Invalid modifier return type: {type(modified).__qualname__}')
        return roll_results


class Dice(namedtuple('_DiceBase', ('number_of_dice', 'sides')), Resolvable):
    """An immutable representation of a dice roll definition.

    .. attribute:: number_of_dice

        The number of dice in this roll.

    .. attribute:: sides

        How many sides the dice in this roll have.

    .. attribute:: modifiers

        Any modifier calls for this dice roll.
    """

    def resolve(self, context):
        return self.roll(context)

    # pylint: disable=missing-raises-doc
    def roll(self, context):
        """Rolls the dice represented by this object.

        :param Dialect context: The context to use.

        :returns: The roll results.
        :rtype: RollResults
        """
        number_of_dice = context[self.number_of_dice]
        if isinstance(number_of_dice, RollResults):
            number_of_dice = number_of_dice.value
        sides = context[self.sides]
        if isinstance(sides, RollResults):
            sides = sides.value
        return RollResults.roll(number_of_dice, sides)

    def __str__(self):
        return f'<Roll: {self.number_of_dice}d{self.sides}>'


class Freeze(namedtuple('_FreezeBase', ('value')), Resolvable):
    """
    """

    def resolve(self, context):
        raise NotImplementedError()


class Length(namedtuple('_LengthBase', ('value')), Resolvable):
    """
    """

    def resolve(self, context):
        raise NotImplementedError()


class Roll(namedtuple('_RollBase', ('value')), Resolvable):
    """
    """

    def resolve(self, context):
        raise NotImplementedError()
