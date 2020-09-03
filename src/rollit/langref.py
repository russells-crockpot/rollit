"""
"""
from collections import namedtuple

from .ast import elements

__all__ = [
    'KEYWORDS',
    'OPERATORS',
    'KEYWORD_SET',
    'SPECIAL_ACCESSORS',
    'SPECIAL_REFERENCES',
    'ATOM_TYPES',
]


class _HolderMixin:

    def __contains__(self, value):
        return value in self.all

    def __len__(self):
        return len(self.all)

    def __iter__(self):
        return iter(self.all)


def _add_all(items, so_far=None):
    if so_far is None:
        so_far = set()
    for item in items:
        if isinstance(item, (list, set, tuple)):
            _add_all(item, so_far)
        else:
            so_far.add(item)
    return so_far


def _create_holder(name, **items):
    base = namedtuple(f'_{name}Base', tuple((*items.keys(), 'all')))
    return type(name, (_HolderMixin, base), {})(
        **items,
        all=_add_all(items.values()),
    )


_conditonal_keywords = _create_holder(
    'ConditionalKeywords',
    start=('use', 'if'),
    body=('then', 'unless', 'otherwise'),
)
_loop_keywords = _create_holder(
    'LoopKeywords',
    start=('until', 'for'),
    body=('every', 'do', 'except', 'when', 'restart', 'at', 'before', 'after'))

_error_handling_keywords = _create_holder(
    'ErrorHandlingKeywords',
    start=('attempt', 'oops'),
    body=('always', 'but', 'when', 'occurrs', 'then', 'if'),
)

KEYWORDS = _create_holder(
    'Keywords',
    load=('load', 'from', 'into'),
    conditional=_conditonal_keywords,
    loop=_loop_keywords,
    error_handling=_error_handling_keywords,
    modifiers=('leave',),
    other=('not', 'and', 'or', 'has', 'isa', 'clear'),
)
"""
"""

KEYWORD_SET = frozenset(KEYWORDS)

OPERATORS = _create_holder(
    'Operators',
    math=('+', '-', '*', '/', '%/', '%'),
    comparison=('>', '<', '==', '!=', '>=', '<=', 'has', 'and', 'or', 'isa'),
    unary=('not',),
    roll=('&', '^'),
    assignment=('=', '+=', '-=', '*=', '/=', '%=', '%/=', '^=', '&='),
    words=('has', 'and', 'or', 'isa', 'not'),
)
"""
"""

SPECIAL_REFERENCES = ('?', '~', '!', '$', '#')
""" """

SPECIAL_ACCESSORS = ('#', '+', '=', '*')
""" """

ATOM_TYPES = (int, float, str, elements.SpecialAccessor, elements.SpecialReference, type(None))
""" """
