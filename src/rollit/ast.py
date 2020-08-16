"""
"""
import enum
import operator
from collections import namedtuple

from lark import Token
from lark.visitors import Transformer

from .dialect import Dialect
from .model import RollResults

__all__ = ['RollWithItTransformer']

_OP_MAP = {
    'STAR': operator.mul,
    'PLUS': operator.add,
    'MINUS': operator.sub,
    'SLASH': operator.floordiv,  #CONSIDER addind way to get remainder, etcetera
}


class _DialectDefPartRole(enum.Enum):
    PARENT = 0
    DEFINED = 1


_DialectDefPart = namedtuple('_DialectDefPart', ('value', 'role'))
_ModifierCall = namedtuple('_ModifierCall', ('func', 'args'))


# pylint: disable=missing-function-docstring
class RollWithItTransformer(Transformer):
    """
    """

    def __init__(self, dialect, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._dialect = dialect

    def roll(self, items):
        num_dice = items[0]
        if isinstance(num_dice, Token):
            num_dice = num_dice.value
        sides = items[1]
        if isinstance(sides, Token):
            sides = sides.value
        results = RollResults(int(num_dice), int(sides))
        for modifier, args in items[2:]:
            modified = modifier(*args, roll=results)
            if isinstance(modified, (set, tuple, list)):
                results.rolls = modified
            elif isinstance(modified, (int, float)):
                results.value = modified
            elif isinstance(modified, RollResults):
                results = modified
            else:
                raise TypeError(f'Invalid modifier return type: {type(modified).__qualname__}')
        return results

    def math(self, items):
        if len(items) == 1:
            if isinstance(items[0], RollResults):
                return items[0]
            return int(items[0]) if items[0] else 0
        left, op, right = items
        if isinstance(left, Token):
            left = left.value
        if isinstance(right, Token):
            right = right.value
        left = int(left)
        right = int(right)
        return _OP_MAP[op.type](left, right)

    def substitution(self, items):
        return self._dialect.get_substitution(items[0].value)

    def alias_def(self, items):
        self._dialect.add_alias(items[0].value, items[1].value)

    def modifier_call(self, items):
        name, *args = items
        if args:
            args = args[0].children
        return _ModifierCall(self._dialect.get_modifier(name.value), args)

    #FIXME with dice rolls, it saves the value of the final roll, not the expression itself.
    def sub_def(self, items):
        name, value = items
        if isinstance(name, Token):
            name = name.value
        if isinstance(value, Token):
            value = int(value.value)
        self._dialect.add_substitution(name, value)

    def _get_relative_dialect(self, name):
        if name == '^':
            if not self._dialect.parent:
                raise Exception()
            return self._dialect.parent
        if name == '~':
            return self._dialect.root
        return None

    def dialect_name(self, items):
        return _DialectDefPart(items[0].value, _DialectDefPartRole.DEFINED)

    def dialect_parent(self, items):
        parent = self._get_relative_dialect(items[0].value)
        if not parent:
            parent = Dialect.get_dialect(parent)
        return _DialectDefPart(parent, _DialectDefPartRole.PARENT)

    def dialect_def(self, items):
        dialect_name = None
        parent = None
        for item in items:
            if item.role == _DialectDefPartRole.PARENT:
                parent = item.value
            elif item.role == _DialectDefPartRole.DEFINED:
                dialect_name = item.value
            else:
                raise Exception()
        dialect = self._get_relative_dialect(dialect_name)
        if dialect and parent:
            raise Exception()
        self._dialect = Dialect.get_or_create_dialect(dialect, parent or self._dialect)

    def dialect_statement(self, items):
        return

    def macro_args(self, items):
        return [item.value.strip() for item in items]

    def macro(self, items):
        name, args = items
        macro = self._dialect.get_macro(name.value)
        macro(*args)
