"""
"""
from rollit.model import SingleValueElement

__all__ = [
    'pformat_model',
    'pprint_model',
]


def pformat_model(elem):
    """
    """

    def _get_lines(item, *, indent=0):
        if isinstance(item, (int, float, str)):
            return str(item)
        preamble = f'{"  "*indent}{type(item).__name__}:'
        if isinstance(item, SingleValueElement):
            value = _get_lines(item.value, indent=indent + 1)
            if isinstance(value, str):
                return [f'{preamble} {value}']
            value.insert(0, preamble)
            return value
        indent += 1
        lines = [preamble]
        for name, value in item._asdict().items():
            value_preamble = f'{"  "*indent}{name}:'
            value = _get_lines(value, indent=indent + 1)
            if isinstance(value, str):
                lines.append(f'{value_preamble} {value}')
            else:
                lines.append(preamble)
                lines += value
        return lines

    if isinstance(elem, list):
        lines = []
        for child in elem:
            child_lines = _get_lines(child, indent=1)
            if isinstance(child_lines, str):
                lines.append(f'- {child_lines}')
                continue
            lines.append(f'- {child_lines[0][2:]}')
            lines += child_lines[1:]
    else:
        lines = _get_lines(elem)
    return '\n'.join(lines)


def pprint_model(elem):
    """
    """
    print(pformat_model(elem))
