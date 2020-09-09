"""
"""
import operator
import re

__all__ = [
    'KEYWORDS',
    'OPERATOR_MAP',
    'MATH_OPERATORS',
    'ESCAPE_STR_PAT',
    'ESCAPE_MAP',
]


def _raise_not_implemented(*args):
    raise NotImplementedError


KEYWORDS = frozenset({
    'after',
    'always',
    'at',
    'attempt',
    'before',
    'but',
    'Clear',
    'do',
    'every',
    'except',
    'for',
    'from',
    'has',
    'if',
    'into',
    'isa',
    'leave',
    'load',
    'not',
    'occurs',
    'oops',
    'otherwise',
    'restart',
    'that',
    'then',
    'unless',
    'until',
    'use',
    'when',
})

OPERATOR_MAP = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
    '%/': operator.truediv,
    '%': operator.mod,
    '>': operator.gt,
    '<': operator.lt,
    '==': operator.eq,
    '!=': operator.ne,
    '>=': operator.ge,
    '<=': operator.le,
    'has': lambda x, y: y in x,
    'and': lambda x, y: 1 if x and y else 0,
    'or': lambda x, y: 1 if x or y else 0,
    'isa': _raise_not_implemented,
    '&': _raise_not_implemented,
}

MATH_OPERATORS = frozenset({'+', '-', '*', '/', '%/', '%'})

ESCAPE_STR_PAT = re.compile(r"\\([\\runftvb'])")
#FIXME Unicode escapes
ESCAPE_MAP = {
    'n': '\n',
    'r': '\r',
    'f': '\f',
    "'": "'",
    'v': '\v',
    'b': '\b',
    '\\': '\\',
}
