"""
"""
import re
from contextlib import suppress

from .elements import StringLiteral, BinaryOp, Negation, SpecialReference, OneSidedOperator, \
        TwoSidedOperator, OverloadOnlyOperator
from ..util import is_valid_iterable, ensure_tuple

__all__ = [
    'was_evaluated',
    'flatten_tuple',
    'negate',
    'get_operator',
]


def was_evaluated(item):
    """
    """
    return (item is None or item == SpecialReference.NONE
            or isinstance(item, (int, bool, float, StringLiteral)))


def flatten_tuple(item):
    """
    """
    if not is_valid_iterable(item):
        return ensure_tuple(item)
    if item and is_valid_iterable(item[0]) and len(item) == 1:
        item = item[0]
    if item and is_valid_iterable(item[0]):
        item = (*item[0], item[1])
    return tuple(item)


# pylint: disable=too-many-function-args
def negate(element, codeinfo=None, script=None):
    """
    """
    if element is None or element == SpecialReference.NONE:
        return 1
    if isinstance(element, (int, float, bool)):
        return 0 if element else 1
    if isinstance(element, StringLiteral):
        return 0 if element.value else 1
    if isinstance(element, Negation):
        return element.value
    if isinstance(element, BinaryOp) and element.op == TwoSidedOperator.NOT_EQUALS:
        return BinaryOp(element.left,
                        TwoSidedOperator.EQUALS,
                        element.right,
                        codeinfo=element.codeinfo)
    return Negation(element, codeinfo=codeinfo)


# pylint: disable=no-value-for-parameter
def get_operator(symbol):
    """
    """
    with suppress(ValueError):
        return OneSidedOperator(symbol)
    with suppress(ValueError):
        return TwoSidedOperator(symbol)
    with suppress(ValueError):
        return OverloadOnlyOperator(re.sub(r'\s+', '', symbol))
    raise ValueError(f'Unknown operator: {symbol}')
