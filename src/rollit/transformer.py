"""
"""
import enum
import operator
from collections import namedtuple
from contextlib import suppress

from .ast import (Resolvable, DefinitionType, Definition, MacroCall, ModifierCall, Substitution,
                  SwitchDialect, Repeat, Math, DiceRoll, Unary)
from ._parser import Token, Transformer, Tree

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


# pylint: disable=missing-function-docstring
class RollWithItTransformer(Transformer):
    """
    """

    @classmethod
    def _values(cls, items):
        if not isinstance(items, Resolvable) and isinstance(items, (tuple, list, set)):
            return tuple(cls._value(item) for item in items)
        return cls._value(items)

    @staticmethod
    def _value(item):
        if not item:
            return item
        if isinstance(item, Tree):
            item = item.children
        if not isinstance(item, Resolvable):
            with suppress(TypeError):
                if len(item) == 1:
                    item = item[0]
        if isinstance(item, Token):
            item = item.value
        try:
            item = int(item)
        except (TypeError, ValueError):
            with suppress(TypeError, ValueError):
                item = float(item)
        return item

    def roll(self, items):
        return DiceRoll(items[0], items[1], items[2:])

    def unary(self, items):
        sign, value = self._values(items)
        if sign == '+':
            return value
        return Unary(sign, value)

    def math(self, items):
        return Math(*self._values(items))

    def substitution(self, items):
        return Substitution(self._value(items))

    def modifier_call(self, items):
        name, args = items
        return ModifierCall(name.value, args)

    def definition(self, items):
        def_token_type = items[0].type
        name, def_ = items[1:]
        if def_token_type.startswith('ALIAS'):
            type_ = DefinitionType.ALIAS
        elif def_token_type.startswith('MODIFIER'):
            type_ = DefinitionType.MODIFIER
        elif def_token_type.startswith('SUBSTITUTION'):
            type_ = DefinitionType.SUBSTITUTION
        return Definition(self._value(name), self._value(def_), type_)

    def switch_dialect(self, items):
        parent = name = None
        for item in items:
            if item.data == 'dialect_parent':
                parent = self._value(item.children[0])
            elif item.data == 'dialect_name':
                name = self._value(item.children[0])
            else:
                raise Exception()
        return SwitchDialect(name, parent)

    def macro_args(self, items):
        return [item.value.strip() for item in items]

    def macro(self, items):
        return MacroCall(self._value(items[0]), items[1])

    def assignment(self, items):
        cp.cyan(items)
        exit()

    def reference(self, items):
        cp.red(items)
        exit()

    def run(self, items):
        cp.green(items)
        exit()

    def args(self, items):
        return tuple(self._value(a) for a in items)
