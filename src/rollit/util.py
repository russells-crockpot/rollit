"""
"""
import functools
from enum import Enum
from rollit.ast import SingleValueElement, ModelElement

__all__ = [
    'pformat_model',
    'pprint_model',
    'unwrap_func',
    'format_runtime_error',
    'is_valid_iterable',
    'ensure_tuple',
]


# pylint: disable=too-complex
def pformat_model(elem):
    """
    """

    # pylint: disable=too-many-return-statements
    def _get_lines(item, *, indent=0):
        if isinstance(item, Enum):
            return str(item)
        preamble = f'{"  "*indent}{type(item).__name__}:'
        if isinstance(item, SingleValueElement):
            value = _get_lines(item.value, indent=indent + 1)
            if isinstance(value, str):
                return [f'{preamble} {value}']
            value.insert(0, preamble)
            return value
        if isinstance(item, ModelElement):
            indent += 1
            lines = [preamble]
            for name, value in item._asdict().items():
                if name == 'codeinfo':
                    continue
                value_preamble = f'{"  "*indent}{name}'
                value = _get_lines(value, indent=indent + 1)
                if isinstance(value, str):
                    lines.append(f'{value_preamble}: {value}')
                else:
                    lines.append(value_preamble)
                    lines += value
            return lines
        if isinstance(item, (set, list, tuple)):
            if not item:
                return repr(item)
            lines = []
            for child in item:
                child_lines = _get_lines(child, indent=indent + 1)
                if isinstance(child_lines, str):
                    lines.append(f'{"  "*indent}- {child_lines}')
                    continue
                lines.append(f'{"  "*indent}- {child_lines[0].strip()}')
                lines += child_lines[1:]
            return lines
        return str(item)

    return '\n'.join(_get_lines(elem))
    # return '\n'.join(l for l in _get_lines(elem) if l.strip().strip('-'))


def pprint_model(elem):
    """
    """
    print(pformat_model(elem))


def unwrap_func(func):
    """
    """
    seen = set()
    while True:
        if id(func) in seen:
            raise RuntimeError(f'Circular reference in unwrapping of function {func}')
        seen.add(id(func))
        if isinstance(func, functools.partial):
            func = func.func
        elif hasattr(func, '__wrapped__'):
            func = func.__wrapped__
        else:
            return func


def format_runtime_error(error):
    """
    """
    lines = [
        f'A {type(error).__name__} occurred!',
        f'  Error Message: {error.msg}',
    ]
    if error.stacktrace:
        lines.append('Stacktrace:')
        for item in error.stacktrace:
            if not item.codeinfo:
                lines.append(f'  Unknown {type(item).__name__}')
            else:
                lines.append(f'  line #{item.codeinfo.lineno:02}: {item.codeinfo.text}')
    return '\n'.join(lines)


def is_valid_iterable(node):
    """
    """
    return isinstance(node, (list, tuple)) and not isinstance(node, ModelElement)


def ensure_tuple(item):
    """
    """
    if is_valid_iterable(item):
        if isinstance(item, tuple):
            return item
        return tuple(item)
    return (item,)
