# pylint: disable=unexpected-keyword-arg,no-value-for-parameter,too-many-public-methods
# pylint: disable=no-member,missing-function-docstring,redefined-outer-name
"""
"""
import functools
import re
from collections import namedtuple
from contextlib import suppress

from . import model
from .exceptions import InvalidNameError
from .grammar import TreeNode

__all__ = ()

_ESCAPE_STR_PAT = re.compile(r"\\([\\runftvb'])")
#FIXME Unicode escapes
_ESCAPE_MAP = {
    'n': '\n',
    'r': '\r',
    'f': '\f',
    "'": "'",
    'v': '\v',
    'b': '\b',
    '\\': '\\',
}

_PredicatedStatement = namedtuple('_PredicatedStatement', ('predicate', 'statement'))


class _BaseInternalSingleValue(tuple):

    def __new__(cls, value):
        return super().__new__(cls, (value,))

    def __str__(self):
        return f'{type(self).__name__}{super().__str__()}'

    def __repr__(self):
        return f'{type(self).__name__}{super().__repr__()}'


_Otherwise = type('_Otherwise', (_BaseInternalSingleValue,), {})
_LoopName = type('_LoopName', (_BaseInternalSingleValue,), {})
_LoopBody = type('_LoopBody', (_BaseInternalSingleValue,), {})
_ItemList = type('_ItemList', (tuple,), {})

_ELEMENT_TYPES = (model.ModelElement, _PredicatedStatement, _BaseInternalSingleValue, _ItemList)


def _is_valid_iterable(node):
    return isinstance(node, (list, tuple)) and not isinstance(node, _ELEMENT_TYPES)


def _unwrap_node(node):
    if _is_valid_iterable(node):
        items = type(node)(nd for nd in (_unwrap_node(n) for n in node) if nd)
        with suppress(TypeError):
            if len(items) == 1 and _is_valid_iterable(node):
                return items[0]
        return items
    if not isinstance(node, TreeNode):
        return node
    elements = _unwrap_node(node.elements)
    with suppress(TypeError):
        if len(elements) == 1 and _is_valid_iterable(node):
            return elements[0]
    return elements


# pylint: disable=too-complex
def elements_to_values(*, text_only=False, elements_only=False, must_have_text=False, unwrap=True):
    """
    """

    def _decorator(func):

        @functools.wraps(func)
        def _wrapper(*args):
            values = []
            for element in args[-1]:
                if isinstance(element, (int, float)):
                    values.append(element)
                    continue
                if not element:
                    continue
                if isinstance(element, TreeNode):
                    if must_have_text and not element.text.strip():
                        continue
                    if elements_only:
                        element = element.elements
                    elif text_only:
                        element = element.text.strip()
                    else:
                        element = element.elements or element.text.strip()
                if element:
                    if unwrap:
                        element = _unwrap_node(element)
                    values.append(element)
            return func(*args[:-1], values)

        return _wrapper

    return _decorator


def _flatten_tuple(item):
    if not _is_valid_iterable(item):
        return _to_tuple(item)
    if item and _is_valid_iterable(item[0]):
        item = (*item[0], item[1])
    return tuple(item)


def _to_tuple(item):
    if isinstance(item, _ELEMENT_TYPES) or not isinstance(item, (list, tuple)):
        return (item,)
    if isinstance(item, list):
        return tuple(item)
    return item


def _negate(element):
    if isinstance(element, model.Negation):
        return element.value
    return model.Negation(element)


# The Actions


@elements_to_values()
def length(text, start, end, values):
    return model.Length(values[0])


@elements_to_values()
def dice(text, start, end, values):
    return model.Dice(*values)


@elements_to_values()
def binary_op(text, start, end, values):
    return model.BinaryOp(*values)


@elements_to_values()
def use_if(text, start, end, values):
    return model.UseIf(*values)


def keyword(text, start, end, values):
    raise InvalidNameError(f'{text[start:end]} is a keyword and cannot be used  .')


@elements_to_values(text_only=True)
def int_(text, start, end, values):
    return int(''.join(values))


@elements_to_values(text_only=True)
def float_(text, start, end, values):
    return float(''.join(values))


@elements_to_values(text_only=True)
def string(text, start, end, values):
    return model.StringLiteral(
        _ESCAPE_STR_PAT.sub(lambda m: _ESCAPE_MAP[m.group(1)], text[start + 1:end - 1]))


def text(text, start, end, values):
    return text[start:end]


def special_ref(text, start, end, values):
    return model.SpecialReference(text[start:end])


def ignore(*args):
    return None


@elements_to_values()
def negate(text, start, end, values):
    return _negate(values[0])


@elements_to_values()
def modifier_call(text, start, end, values):
    if len(values) == 1:
        return model.ModifierCall(modifier=values[0], args=())
    return model.ModifierCall(modifier=values[0], args=_to_tuple(values[-1]))


@elements_to_values()
def modify(text, start, end, values):
    return model.Modify(subject=values[0], modifiers=_to_tuple(values[-1]))


@elements_to_values()
def arg_list(text, start, end, values):
    return _flatten_tuple(values)


@elements_to_values()
def access(text, start, end, values):
    return model.Access(accessing=values[0], accessors=_to_tuple(values[-1]))


@elements_to_values()
def reduce(text, start, end, values):
    value = values[0]
    if value == '*':
        value = model.SpecialReference.ALL
    return model.Reduce(value)


@elements_to_values()
def enlarge(text, start, end, values):
    size = value = None
    sep_idx = values.index('@')
    with suppress(IndexError):
        size = values[:sep_idx][0]
    with suppress(IndexError):
        value = values[sep_idx + 1:][0]
    return model.Enlarge(size=size, value=value)


@elements_to_values()
def assignment(text, start, end, values):
    target, op, value = values
    if len(op) > 1:
        value = model.BinaryOp(left=target, op=op[:-1], right=value)
    return model.Assignment(target=target, value=value)


def leave(*args):
    return model.SingleWordStatment.LEAVE


@elements_to_values()
def predicated_statement(text, start, end, values):
    return _PredicatedStatement(*values)


@elements_to_values()
def otherwise(text, start, end, values):
    return _Otherwise(values[-1])


@elements_to_values()
def create_bag(text, start, end, values):
    return tuple(model.CreateBag(item) for item in _to_tuple(values[-1]))


@elements_to_values()
def load_from_into(text, start, end, values):
    to_load, load_from, *into = values
    if into:
        into = into[0]
    else:
        into = model.SpecialReference.ROOT
    if to_load == '*':
        to_load = model.SpecialReference.ALL
    items = []
    if _is_valid_iterable(load_from):
        for item in _flatten_tuple(load_from):
            items.append(model.Load(
                to_load=to_load,
                load_from=item,
                into=into,
            ))
    else:
        for item in _flatten_tuple(to_load):
            items.append(model.Load(
                to_load=item,
                load_from=load_from,
                into=into,
            ))
    return items[0] if len(items) == 1 else tuple(items)


@elements_to_values()
def load_from(text, start, end, values):
    to_load, load_from = values
    if _is_valid_iterable(to_load):
        to_load = _flatten_tuple(to_load)
    else:
        to_load = (to_load,)
    items = []
    for item_to_load in to_load:
        items.append(
            model.Load(
                to_load=item_to_load,
                load_from=load_from,
                into=model.SpecialReference.ROOT,
            ))
    return items[0] if len(items) == 1 else tuple(items)


@elements_to_values()
def load_into(text, start, end, values):
    to_load, into = values
    items = []
    for load_from in _flatten_tuple(to_load):
        items.append(model.Load(
            to_load=model.SpecialReference.ALL,
            load_from=load_from,
            into=into,
        ))
    return items[0] if len(items) == 1 else tuple(items)


@elements_to_values()
def load(text, start, end, values):
    if _is_valid_iterable(values[0]):
        values = _flatten_tuple(values[0])
    items = []
    for item in values:
        items.append(model.Load(
            to_load=model.SpecialReference.ALL,
            load_from=item,
            into=item,
        ))
    return items[0] if len(items) == 1 else tuple(items)


# pylint: disable=protected-access
@elements_to_values()
def restart(text, start, end, values):
    location_specifier = model.RestartLocationSpecifier(values[0])
    target = model.SpecialReference.NONE
    with suppress(IndexError):
        target = values[1]
    if isinstance(target, model.SpecialReference):
        return getattr(model.Restart, f'{location_specifier._name_}_{target._name_}')
    return model.Restart(location_specifier=location_specifier, target=target)


@elements_to_values()
def if_stmt(text, start, end, values):
    if_ = values.pop(0)
    otherwise = unlesses = None
    with suppress(IndexError):
        otherwise = values.pop(-1)
        if isinstance(otherwise, _Otherwise):
            otherwise = otherwise[0]
            if values:
                unlesses = _to_tuple(values[0])
        else:
            unlesses = _to_tuple(otherwise)
            otherwise = None
    rval = model.If(
        predicate=if_.predicate,
        then=if_.statement,
        otherwise=otherwise,
    )
    if unlesses:
        previous = otherwise
        for unless in unlesses:
            previous = model.If(predicate=unless.predicate,
                                then=unless.statement,
                                otherwise=previous)
        rval = model.If(
            predicate=_negate(rval.predicate),
            then=previous,
            otherwise=rval.then,
        )
    return rval


@elements_to_values()
def loop_name(text, start, end, values):
    return _LoopName(values[0])


@elements_to_values()
def loop_body(text, start, end, values):
    return _LoopBody(values[0])


@elements_to_values()
def until_do(text, start, end, values):
    name = until = do = otherwise = None
    if isinstance(values[0], _LoopName):
        name = values.pop(0)[0]
    until = values.pop(0)
    do = values.pop(0)[0]
    if values and isinstance(values[-1], _Otherwise):
        otherwise = values.pop(-1)[0]
    if values:
        for except_when in _to_tuple(values[0]):
            do = model.If(predicate=except_when.predicate, then=except_when.statement, otherwise=do)
    return model.UntilDo(
        name=name,
        until=until,
        do=do,
        otherwise=otherwise,
    )


@elements_to_values()
def for_every(text, start, end, values):
    loop_name = None
    if isinstance(values[0], _LoopName):
        loop_name = values.pop(0)[0]
    return model.ForEvery(
        name=loop_name,
        item_name=values[0],
        iterable=values[1],
        do=values[-1][0],
    )


@elements_to_values()
def modifier_def(text, start, end, values):
    target, params, *definition = values
    params = _flatten_tuple(params)
    seen = set()
    for param in params:
        if param in seen:
            #TODO pretty print target
            raise InvalidNameError(f'Parameter {param} of modifier {target} is '
                                   'defined more than once!')
        seen.add(param)
    if definition:
        definition = definition[0]
    else:
        definition = None
    return model.ModifierDef(
        target=target,
        parameters=params,
        definition=definition,
    )


@elements_to_values()
def block(text, start, end, values):
    if _is_valid_iterable(values[0]):
        return _flatten_tuple(values[0])
    return values[0]


def empty_block(*args):
    return ()


@elements_to_values()
def statements(text, start, end, values):
    return values
