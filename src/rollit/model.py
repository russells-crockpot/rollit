"""
"""
import operator
from abc import ABCMeta, abstractmethod
from collections import namedtuple
from contextlib import suppress

from .elements import RollResults


class ModelElement(metaclass=ABCMeta):
    """
    """
    singleton = False
    accepts_none = False
    __slots__ = ()

    @abstractmethod
    def resolve(self, context):
        """
        """


# pylint: disable=abstract-method
class SingletonElement(tuple, ModelElement):
    """
    """
    singleton = True

    def __new__(cls, value):
        with suppress(AttributeError, TypeError):
            value = value['value']
        if isinstance(value, (str, ModelElement)) or not hasattr(value, '__iter__'):
            value = (value,)
        return super().__new__(cls, value)

    @property
    def value(self):
        """
        """
        return self[0]

    @property
    def _fields(self):
        return ('value',)

    def _asdict(self):
        return {'value', self.value}

    def __str__(self):
        return f'<{type(self).__name__}: {self.value}>'

    def __repr__(self):
        return f'{type(self).__name__}({repr(self.value)})'


class Reference(SingletonElement):
    """
    """

    def resolve(self, context):
        return context.dialect.get_variable(self.value)


class Assignment(namedtuple('_AssignmentBase', ('name', 'value')), ModelElement):
    """
    """

    def resolve(self, context):
        context.dialect.add_variable(self.name, context[self.value])


class Load(namedtuple('_LoadBase', ('dialects',)), ModelElement):
    """
    """

    def resolve(self, context):
        raise NotImplementedError()


class Math(namedtuple('_MathBase', ('left', 'op', 'right')), ModelElement):
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


class ModifierCall(namedtuple('_ModifierCallBase', ('modifier', 'args')), ModelElement):
    """
    """

    def resolve(self, context):
        # args = (context[a] for a in self.args)
        # return context.current_dialect.get_modifier(self.name)
        raise NotImplementedError()


class Modify(namedtuple('_ModifyBase', ('modifying', 'modifiers')), ModelElement):
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


class Dice(namedtuple('_DiceBase', ('number_of_dice', 'sides')), ModelElement):
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


class Length(SingletonElement):
    """
    """

    def resolve(self, context):
        raise NotImplementedError()


class Roll(SingletonElement):
    """
    """
    accepts_none = True

    def resolve(self, context):
        raise NotImplementedError()


class Access(namedtuple('_AccessBase', ('accessing', 'accessors')), ModelElement):
    """
    """

    def resolve(self, context):
        raise NotImplementedError()


class LoadFrom(namedtuple('_LoadFromBase', ('loadables', 'dialect')), ModelElement):
    """
    """

    def resolve(self, context):
        raise NotImplementedError()


def statement(value):
    """
    """
    if isinstance(value, str):
        return None
    return value


statement.singleton = True
statement.accepts_none = True


def blocks(value):
    """
    """
    if 'statements' not in value:
        return value
    return value['statements']


blocks.singleton = True
blocks.accepts_none = True


class Fill(namedtuple('_FillBase', ('size', 'value')), ModelElement):
    """
    """

    def resolve(self, context):
        raise NotImplementedError()


class RollMath(namedtuple('_RollMathBase', ('left', 'op', 'right')), ModelElement):
    """
    """

    def resolve(self, context):
        raise NotImplementedError()


class Comparison(namedtuple('_ComparisonBase', ('left', 'op', 'right')), ModelElement):
    """
    """

    def resolve(self, context):
        raise NotImplementedError()


class Negation(SingletonElement):
    """
    """

    def resolve(self, context):
        raise NotImplementedError()


class If(namedtuple('_IfBase', ('predicate', 'then', 'otherwise')), ModelElement):
    """
    """

    def resolve(self, context):
        raise NotImplementedError()


class UseIf(namedtuple('_UseIfBase', ('if_true', 'predicate', 'if_false')), ModelElement):
    """
    """

    def resolve(self, context):
        raise NotImplementedError()


class DoUntil(namedtuple('_DoUntilBase', ('do', 'until', 'otherwise')), ModelElement):
    """
    """

    def resolve(self, context):
        raise NotImplementedError()


class UntilDo(namedtuple('_UntilDoBase', ('until', 'do', 'otherwise')), ModelElement):
    """
    """

    def resolve(self, context):
        raise NotImplementedError()


# class X(namedtuple('_XBase', ('',)), ModelElement):
#     """
#     """
#
#     def resolve(self, context):
#         raise NotImplementedError()
