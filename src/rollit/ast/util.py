"""
"""

from .base import ModelElement, CodeInfo
from .elements import StringLiteral, BinaryOp, Negation, SpecialReference

__all__ = [
    'was_evaluated',
    'is_valid_iterable',
    'flatten_tuple',
    'to_tuple',
    'negate',
]


def was_evaluated(item):
    """
    """
    return (item is None or item == SpecialReference.NONE
            or isinstance(item, (int, bool, float, StringLiteral)))


def is_valid_iterable(node):
    """
    """
    return isinstance(node, (list, tuple)) and not isinstance(node, ModelElement)


def flatten_tuple(item):
    """
    """
    if not is_valid_iterable(item):
        return to_tuple(item)
    if item and is_valid_iterable(item[0]):
        item = (*item[0], item[1])
    return tuple(item)


def to_tuple(item):
    """
    """
    if isinstance(item, ModelElement) or not isinstance(item, (list, tuple)):
        return (item,)
    if isinstance(item, list):
        return tuple(item)
    return item


# pylint: disable=too-many-function-args
def negate(element, codeinfo=None):
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
    if isinstance(element, BinaryOp) and element.op == '!=':
        start_pos = element.codeinfo.start_pos if not codeinfo else codeinfo.start_pos
        return BinaryOp(element.left,
                        '==',
                        element.right,
                        codeinfo=CodeInfo(element.codeinfo.script, start_pos,
                                          element.codeinfo.end_pos))
    return Negation(element, codeinfo=codeinfo)
