# pylint: disable=unexpected-keyword-arg,no-value-for-parameter,too-many-public-methods
# pylint: disable=no-member,missing-function-docstring,redefined-outer-name,unsubscriptable-object
# pylint: disable=too-many-function-args
"""
"""
import functools
from contextlib import suppress

from . import constants, elements, internal, util
from .base import CodeInfo
from .. import langref
from ..exceptions import InvalidNameError
from ..grammar import TreeNode

__all__ = ()


# pylint: disable=too-many-return-statements
def _unwrap_node(node):
    if node is None:
        return None
    if util.is_valid_iterable(node):
        items = type(node)(
            nd for nd in (_unwrap_node(n) for n in node) if nd or isinstance(nd, (int, float)))
        with suppress(TypeError):
            if len(items) == 1 and util.is_valid_iterable(node):
                return items[0]
        return items
    if not isinstance(node, TreeNode):
        return node
    if not node.elements:
        return node.text
    elements = _unwrap_node(node.elements)
    with suppress(TypeError):
        if len(elements) == 1 and util.is_valid_iterable(node):
            return elements[0]
    return elements


def elements_to_values(func):
    """
    """

    @functools.wraps(func)
    def _wrapper(*args):
        values = []
        for element in args[-1]:
            if isinstance(element, TreeNode):
                element = element.elements or element.text.strip()
                if element:
                    element = _unwrap_node(element)
            if element or isinstance(element, (int, float)):
                values.append(element)
        return func(*args[:-1], values)

    return _wrapper


def add_codeinfo(func):
    """
    """

    @functools.wraps(func)
    def _wrapper(text, start, end, values):
        #TODO account for \r and \f
        lineno = text[:start].count('\n') + 1
        return func(text, start, end, values, CodeInfo(text[start:end], start, end, lineno))

    return _wrapper


# The Actions


@elements_to_values
@add_codeinfo
def dice(text, start, end, values, codeinfo):
    return elements.DiceNode(*values, codeinfo=codeinfo)


@elements_to_values
@add_codeinfo
def binary_op(text, start, end, values, codeinfo):
    left, op, right = values
    if isinstance(left, (int, float)) and isinstance(right, (int, float)):
        return constants.OPERATOR_MAP[op](left, right)
    if isinstance(left, elements.StringLiteral) and isinstance(right, elements.StringLiteral):
        #TODO they maybe chained
        return elements.StringLiteral((left, right),
                                      codeinfo=CodeInfo(
                                          text[left.codeinfo.start_pos:right.codeinfo.end_pos],
                                          left.codeinfo.start_pos, right.codeinfo.end_pos))
    return elements.BinaryOp(left, op, right, codeinfo=codeinfo)


@elements_to_values
@add_codeinfo
def use_if(text, start, end, values, codeinfo):
    return elements.UseIf(*values, codeinfo=codeinfo)


@add_codeinfo
def basic_name(text, start, end, values, codeinfo):
    name = text[start:end]
    if name in elements.KEYWORDS:
        raise InvalidNameError(f'{name} is a keyword and cannot be used.', codeinfo=codeinfo)
    return name


def int_(text, start, end, elements):
    return int(''.join(text[start:end]))


def float_(text, start, end, elements):
    return float(''.join(text[start:end]))


@add_codeinfo
def string(text, start, end, values, codeinfo):
    return elements.StringLiteral(
        constants.ESCAPE_STR_PAT.sub(lambda m: constants.ESCAPE_MAP[m.group(1)],
                                     text[start + 1:end - 1]),
        codeinfo=codeinfo,
    )


def special_entry(text, start, end, values):
    return elements.SpecialEntry(text[start:end])


def special_accessor(text, start, end, values):
    return elements.SpecialAccessor(text[start:end])


def special_ref(text, start, end, values):
    return elements.SpecialReference(text[start:end])


@add_codeinfo
def reference(text, start, end, values, codeinfo):
    value = text[start:end]
    if value in langref.KEYWORD_SET:
        return None
    return elements.Reference(value, codeinfo=codeinfo)


def text(text, start, end, values):
    return text[start:end]


def ignore(*args):
    return None


@elements_to_values
@add_codeinfo
def negate(text, start, end, values, codeinfo):
    return util.negate(values[0], codeinfo=codeinfo, script=text)


@elements_to_values
@add_codeinfo
def normal_modifier_body(text, start, end, values, codeinfo):
    params = body = ()
    if values and util.is_valid_iterable(values[0]):
        values = values[0]
    if values and isinstance(values[0], internal.ItemList):
        params = tuple(values.pop(0))
    if values:
        body = values[0]
        if not util.is_valid_iterable(body):
            body = (body,)
        else:
            body = util.flatten_tuple(body)
    return params, body


@add_codeinfo
def small_modifier_body(text, start, end, values, codeinfo):
    params, body = normal_modifier_body(text, start, end, values)
    return params, elements.Assignment(
        target=elements.SpecialReference.SUBJECT,
        value=body[0],
        codeinfo=codeinfo,
    )


@elements_to_values
@add_codeinfo
def modifier_def(text, start, end, values, codeinfo):
    target, (params, body) = values
    seen = set()
    for param in params:
        if param in seen:
            #TODO pretty print target
            raise InvalidNameError(
                f'Parameter {param} of modifier {target} is '
                'defined more than once!',
                codeinfo=codeinfo)
        seen.add(param)
    return elements.ModifierDef(
        target=target,
        parameters=params,
        definition=body,
        codeinfo=codeinfo,
    )


@elements_to_values
@add_codeinfo
def first_modifier_call(text, start, end, values, codeinfo):
    target, op, call = values
    if op == '+':
        accessing = target
        accessors = []
        if isinstance(target, elements.Access):
            accessing = target.accessing
            accessors = list(target.accessors)
        if isinstance(call.modifier, elements.Reference):
            accessors.append(call.modifier)
        elif isinstance(call.modifier, elements.Access):
            accessors.append(call.modifier.accessing)
            accessors.extend(call.modifier.accessors)
        call = call._replace(modifier=elements.Access(
            accessing=accessing,
            accessors=tuple(accessors),
            codeinfo=call.codeinfo,
        ))
    return (target, call)


@elements_to_values
@add_codeinfo
def modifier_call(text, start, end, values, codeinfo):
    if len(values) == 1:
        return elements.ModifierCall(modifier=values[0], args=(), codeinfo=codeinfo)
    return elements.ModifierCall(
        modifier=values[0],
        args=util.to_tuple(values[-1]),
        codeinfo=codeinfo,
    )


@elements_to_values
@add_codeinfo
def modify(text, start, end, values, codeinfo):
    (subject, first_call), *other_calls = values
    calls = [first_call]
    if other_calls:
        if util.is_valid_iterable(other_calls[0]):
            calls += other_calls[0]
        else:
            calls.append(other_calls[0])
    return elements.Modify(subject=subject, modifiers=tuple(calls), codeinfo=codeinfo)


@elements_to_values
def param_list(text, start, end, values):
    return internal.ItemList(p.value for p in util.flatten_tuple(values))


@elements_to_values
def arg_list(text, start, end, values):
    return util.flatten_tuple(values)


@elements_to_values
@add_codeinfo
def raw_accessor(text, start, end, values, codeinfo):
    return elements.RawAccessor(values[0], codeinfo=codeinfo)


@elements_to_values
@add_codeinfo
def access(text, start, end, values, codeinfo):
    return elements.Access(accessing=values[0],
                           accessors=util.to_tuple(values[-1]),
                           codeinfo=codeinfo)


@elements_to_values
@add_codeinfo
def reduce(text, start, end, values, codeinfo):
    value = values[0]
    if value == '*':
        value = elements.SpecialReference.ALL
    return elements.Reduce(value, codeinfo=codeinfo)


@elements_to_values
@add_codeinfo
def enlarge(text, start, end, values, codeinfo):
    size = value = None
    sep_idx = values.index('@')
    with suppress(IndexError):
        size = values[:sep_idx][0]
    with suppress(IndexError):
        value = values[sep_idx + 1:][0]
    return elements.Enlarge(size=size, value=value, codeinfo=codeinfo)


@elements_to_values
@add_codeinfo
def modify_and_assign(text, start, end, values, codeinfo):
    return (elements.Assignment(
        target=values[0],
        value=elements.Modify(subject=values[0],
                              modifiers=util.flatten_tuple(values[1:]),
                              codeinfo=codeinfo),
        codeinfo=codeinfo,
    ))


@elements_to_values
@add_codeinfo
def assignment(text, start, end, values, codeinfo):
    target, op, value = values
    if len(op) > 1:
        value = elements.BinaryOp(left=target, op=op[:-1], right=value, codeinfo=codeinfo)
    if target == value:
        return None
    return elements.Assignment(target=target, value=value, codeinfo=codeinfo)


@elements_to_values
@add_codeinfo
def reduce_and_assign(text, start, end, values, codeinfo):
    return elements.Assignment(target=values[0],
                               value=elements.Reduce(values[0], codeinfo=codeinfo),
                               codeinfo=codeinfo)


@add_codeinfo
def leave(text, start, end, values, codeinfo):
    return elements.Leave(codeinfo=codeinfo)


@elements_to_values
@add_codeinfo
def predicated_statement(text, start, end, values, codeinfo):
    return internal.PredicatedStatement(*values, codeinfo=codeinfo)


@elements_to_values
@add_codeinfo
def otherwise(text, start, end, values, codeinfo):
    return internal.Otherwise(values[-1], codeinfo=codeinfo)


@elements_to_values
@add_codeinfo
def new_bag(text, start, end, values, codeinfo):
    if not values:
        return elements.NewBag((), codeinfo=codeinfo)
    return elements.NewBag(util.flatten_tuple(values), codeinfo=codeinfo)


@elements_to_values
@add_codeinfo
def clear(text, start, end, values, codeinfo):
    return elements.ClearValue(values[0], codeinfo=codeinfo)


@elements_to_values
@add_codeinfo
def load_from_into(text, start, end, values, codeinfo):
    to_load, load_from, *into = values
    if into:
        into = into[0]
    else:
        into = elements.SpecialReference.ROOT
    if to_load == '*':
        to_load = elements.SpecialReference.ALL
    items = []
    if util.is_valid_iterable(load_from):
        for item in util.flatten_tuple(load_from):
            items.append(
                elements.Load(
                    to_load=to_load,
                    load_from=item,
                    into=into,
                    codeinfo=codeinfo,
                ))
    else:
        for item in util.flatten_tuple(to_load):
            items.append(
                elements.Load(
                    to_load=item,
                    load_from=load_from,
                    into=into,
                    codeinfo=codeinfo,
                ))
    return items[0] if len(items) == 1 else tuple(items)


@elements_to_values
@add_codeinfo
def load_from(text, start, end, values, codeinfo):
    to_load, load_from = values
    if util.is_valid_iterable(to_load):
        to_load = util.flatten_tuple(to_load)
    else:
        to_load = (to_load,)
    items = []
    for item_to_load in to_load:
        items.append(
            elements.Load(
                to_load=item_to_load,
                load_from=load_from,
                into=elements.SpecialReference.ROOT,
                codeinfo=codeinfo,
            ))
    return items[0] if len(items) == 1 else tuple(items)


@elements_to_values
@add_codeinfo
def load_into(text, start, end, values, codeinfo):
    to_load, into = values
    items = []
    for load_from in util.flatten_tuple(to_load):
        items.append(
            elements.Load(
                to_load=elements.SpecialReference.ALL,
                load_from=load_from,
                into=into,
                codeinfo=codeinfo,
            ))
    return items[0] if len(items) == 1 else tuple(items)


@elements_to_values
@add_codeinfo
def load(text, start, end, values, codeinfo):
    if util.is_valid_iterable(values[0]):
        values = util.flatten_tuple(values[0])
    items = []
    for item in values:
        items.append(
            elements.Load(
                to_load=elements.SpecialReference.ALL,
                load_from=item,
                into=item,
                codeinfo=codeinfo,
            ))
    return items[0] if len(items) == 1 else tuple(items)


# pylint: disable=protected-access
@elements_to_values
@add_codeinfo
def restart(text, start, end, values, codeinfo):
    location_specifier = elements.RestartLocationSpecifier(values[0])
    target = elements.SpecialReference.NONE
    with suppress(IndexError):
        target = values[1]
    return elements.Restart(
        location_specifier=location_specifier,
        target=target,
        codeinfo=codeinfo,
    )


def _process_if_stmt(predicate, then, otherwise, codeinfo):
    rval = elements.IfThen(
        predicate=predicate,
        then=then,
        otherwise=otherwise,
        codeinfo=codeinfo,
    )
    if rval == then:
        return rval
    if rval == otherwise:
        return internal.Otherwise(rval, codeinfo=codeinfo)
    return rval


@elements_to_values
@add_codeinfo
def if_stmt(text, start, end, values, codeinfo):
    if_ = values.pop(0)
    otherwise = unlesses = None
    with suppress(IndexError):
        otherwise = values.pop(-1)
        if isinstance(otherwise, internal.Otherwise):
            otherwise = otherwise.value
            if values:
                unlesses = util.to_tuple(values[0])
        else:
            unlesses = util.to_tuple(otherwise)
            otherwise = None
    rval = _process_if_stmt(if_.predicate, if_.statement, otherwise, codeinfo=codeinfo)
    if rval == if_.statement:
        return rval
    if unlesses:
        previous = otherwise
        for unless in unlesses:
            previous = _process_if_stmt(unless.predicate, unless.statement, previous,
                                        unless.codeinfo)
            if previous == unless.statement:
                return previous
            if isinstance(previous, internal.Otherwise):
                previous = previous[0]
        if not rval or isinstance(rval, internal.Otherwise):
            return previous
        rval = elements.IfThen(
            predicate=util.negate(if_.predicate, codeinfo, text),
            then=previous,
            otherwise=if_.statement,
            codeinfo=codeinfo,
        )
    if isinstance(rval, internal.Otherwise):
        return rval.value
    return rval


@elements_to_values
@add_codeinfo
def loop_name(text, start, end, values, codeinfo):
    return internal.LoopName(values[0], codeinfo=codeinfo)


@elements_to_values
@add_codeinfo
def loop_body(text, start, end, values, codeinfo):
    return internal.LoopBody(values[0], codeinfo=codeinfo)


@elements_to_values
@add_codeinfo
def until_do(text, start, end, values, codeinfo):
    name = until = do = otherwise = None
    if isinstance(values[0], internal.LoopName):
        name = values.pop(0)[0]
    until = values.pop(0)
    do = values.pop(0)[0]
    if values and isinstance(values[-1], internal.Otherwise):
        otherwise = values.pop(-1).value
    if values:
        for except_when in util.to_tuple(values[0]):
            do = elements.IfThen(
                predicate=except_when.predicate,
                then=except_when.statement,
                otherwise=do,
                codeinfo=except_when.codeinfo,
            )
    return elements.UntilDo(
        name=name,
        until=until,
        do=do,
        otherwise=otherwise,
        codeinfo=codeinfo,
    )


@elements_to_values
@add_codeinfo
def for_every(text, start, end, values, codeinfo):
    loop_name = None
    if isinstance(values[0], internal.LoopName):
        loop_name = values.pop(0)[0]
    return elements.ForEvery(
        name=loop_name,
        item_name=values[0],
        iterable=values[1],
        do=values[-1][0],
        codeinfo=codeinfo,
    )


@elements_to_values
@add_codeinfo
def block(text, start, end, values, codeinfo):
    if util.is_valid_iterable(values[0]):
        return util.flatten_tuple(values[0])
    return values[0]


def empty_block(*args):
    return ()


@elements_to_values
@add_codeinfo
def but_if(text, start, end, values, codeinfo):
    predicate, statement = values
    if predicate == '*':
        predicate = elements.SpecialReference.ALL
    return elements.ButIf(predicate, statement, codeinfo=codeinfo)


@elements_to_values
@add_codeinfo
def always(text, start, end, values, codeinfo):
    return internal.Always(values[0])


@elements_to_values
@add_codeinfo
def attempt(text, start, end, values, codeinfo):
    attempt, *buts, always = values
    if not isinstance(always, internal.Always):
        buts = tuple((*buts, always))
        always = None
    else:
        always = always[0]
    if buts and util.is_valid_iterable(buts[0]):
        buts = buts[0]
    return elements.Attempt(
        attempt=attempt,
        buts=buts,
        always=always,
        codeinfo=codeinfo,
    )


@elements_to_values
@add_codeinfo
def oops(text, start, end, values, codeinfo):
    return elements.Oops(values[0], codeinfo=codeinfo)


@elements_to_values
def statements(text, start, end, values):
    return values
