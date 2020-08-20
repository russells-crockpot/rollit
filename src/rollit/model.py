"""
"""
import enum
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


class ModelConstant(enum.Enum):
    """
    """

    @property
    def _fields(self):
        return ('value',)

    @property
    def value(self):
        """
        """
        # pylint: disable=no-member
        return self._value_

    # pylint: disable=missing-docstring
    def resolve(self, context):
        raise NotImplementedError()


ModelElement.register(ModelConstant)


class FlowControl(ModelConstant):
    """
    """
    SKIP = 'skip'
    """ """
    BREAK = 'break'
    """ """

    # pylint: disable=missing-docstring
    def resolve(self, context):
        raise NotImplementedError()


class Reference(SingletonElement):
    """
    """

    def resolve(self, context):
        return context.dialect.get_variable(self.value)


class Assignment(namedtuple('_AssignmentBase', ('target', 'value')), ModelElement):
    """
    """

    def __new__(cls, target, value):
        if isinstance(target, Reference):
            target = target.value
        return super().__new__(cls, target, value)

    def resolve(self, context):
        raise NotImplementedError()


def load(*, to_load, from_dialect=None, into=None):
    """
    """
    if not from_dialect:
        return Load(dialects=to_load, into=into)
    return LoadFrom(to_load=to_load, from_dialect=from_dialect, into=into)


load.singleton = False
load.accepts_none = False


class LoadFrom(namedtuple('_LoadFromBase', ('to_load', 'from_dialect', 'into')), ModelElement):
    """
    """

    def resolve(self, context):
        raise NotImplementedError()


class Load(namedtuple('_LoadBase', ('dialects', 'into')), ModelElement):
    """
    """

    def resolve(self, context):
        raise NotImplementedError()


class Math(namedtuple('_MathBase', ('left', 'op', 'right')), ModelElement):
    """
    """

    def resolve(self, context):
        raise NotImplemented()

    def __str__(self):
        return f'<{type(self).__qualname__}: {self.left} {self.op} {self.right}>'


class ModifierCall(namedtuple('_ModifierCallBase', ('modifier', 'args')), ModelElement):
    """
    """

    def __new__(cls, modifier, args):
        if args:
            args = args[0]
        return super().__new__(cls, modifier, args)

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

    def __new__(cls, ast):
        if isinstance(ast, list) and len(ast) == 2 \
                and ast[0] == '#' and isinstance(ast[1], ModelElement):
            return super().__new__(cls, ast[1])
        return ast

    def resolve(self, context):
        raise NotImplementedError()


class Access(namedtuple('_AccessBase', ('accessing', 'accessors')), ModelElement):
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


class Reduce(SingletonElement):
    """
    """
    accepts_none = True

    def __new__(cls, value):
        if isinstance(value, Enlarge):
            return value
        return super().__new__(cls, value)

    def resolve(self, context):
        raise NotImplementedError()


class Enlarge(namedtuple('_EnlargeBase', ('size', 'value')), ModelElement):
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


class ExceptWhen(namedtuple('_ExceptWhenBase', ('predicate', 'then')), ModelElement):
    """
    """

    def resolve(self, context):
        raise NotImplementedError()


class Unless(namedtuple('_UnlessBase', ('predicate', 'then')), ModelElement):
    """
    """

    def resolve(self, context):
        raise NotImplementedError()


class If(namedtuple('_IfBase', ('predicate', 'then', 'unless', 'otherwise')), ModelElement):
    """
    """

    def __new__(cls, predicate, then, unless=(), otherwise=None):
        return super().__new__(cls, predicate, then, unless, otherwise)

    def resolve(self, context):
        raise NotImplementedError()


class UseIf(namedtuple('_UseIfBase', ('use', 'predicate', 'otherwise')), ModelElement):
    """
    """

    def resolve(self, context):
        raise NotImplementedError()


class DoUntil(namedtuple('_DoUntilBase', ('do', 'until', 'except_when', 'otherwise')),
              ModelElement):
    """
    """

    def __new__(cls, *, do, until, except_when=(), otherwise=None):
        return super().__new__(cls,
                               do=do,
                               until=until,
                               except_when=except_when,
                               otherwise=otherwise)

    def resolve(self, context):
        raise NotImplementedError()


class UntilDo(namedtuple('_UntilDoBase', ('until', 'do', 'except_when', 'otherwise')),
              ModelElement):
    """
    """

    def __new__(cls, until, do, except_when=(), otherwise=None):
        return super().__new__(cls,
                               until=until,
                               do=do,
                               except_when=except_when,
                               otherwise=otherwise)

    def resolve(self, context):
        raise NotImplementedError()


class ModifierDef(namedtuple('_ModifierDefBase', ('target', 'parameters', 'definition')),
                  ModelElement):
    """
    """

    def __new__(cls, *, target, body):
        parameters = body.get('parameters') or ()
        definition = body.get('definition') or ()
        if isinstance(target, Reference):
            target = target.value
        parameters = tuple(p.value if isinstance(p, Reference) else p for p in parameters)
        return super().__new__(cls, target=target, parameters=parameters, definition=definition)

    def resolve(self, context):
        raise NotImplementedError()


# class X(namedtuple('_XBase', ('',)), ModelElement):
#     """
#     """
#
#     def resolve(self, context):
#         raise NotImplementedError()

STATEMENT_KEYWORDS = {
    'skip': FlowControl.SKIP,
    'break': FlowControl.BREAK,
}
"""Keywords that are also a full statement."""
