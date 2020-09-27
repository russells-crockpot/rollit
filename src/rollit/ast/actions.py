# pylint: disable=unexpected-keyword-arg,no-value-for-parameter,too-many-public-methods
# pylint: disable=no-member,missing-function-docstring,redefined-outer-name,unsubscriptable-object
# pylint: disable=too-many-function-args
"""
"""
import functools
from collections import namedtuple
from contextlib import suppress

from . import constants, elements, internal, util
from .base import CodeInfo, preevaluate_predicate, DeferEvaluation
from .. import langref
from ..exceptions import InvalidNameError
from ..grammar import TreeNode
from ..util import is_valid_iterable, ensure_tuple

__all__ = ()


# pylint: disable=too-many-return-statements, too-complex
def _unwrap_node(node):
    if node is None:
        return None
    if is_valid_iterable(node):
        items = []
        for child in node:
            if child is None:
                continue
            if isinstance(child, TreeNode):
                child = _unwrap_node(child)
            if isinstance(child, (int, float)) or child:
                items.append(child)
        if len(items) == 1:
            return items[0]
        return tuple(items)
    if not isinstance(node, TreeNode):
        return node
    if not node.elements:
        return node.text
    elements = _unwrap_node(node.elements)
    with suppress(TypeError):
        if len(elements) == 1 and is_valid_iterable(node):
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
    def _wrapper(self, text, start, end, values):
        if not self.source_code:
            self.source_code = text
        return func(self, text, start, end, values, self.get_codeinfo(start, end))

    return _wrapper


class Actions:
    """
    """
    __slots__ = (
        'lines',
        'source',
    )
    LineInfo = namedtuple('LineInfo', ('start', 'end', 'number', 'content'))

    def __init__(self, source):
        self.source = source
        self.lines = None

    @property
    def source_code(self):
        """
        """
        if self.lines is None:
            return None
        return '\n'.join(l.content for l in self.lines)

    @source_code.setter
    def source_code(self, value):
        if self.lines is not None:
            return
        lines = []
        current_pos = 0
        for i, line in enumerate(value.splitlines()):
            lines.append(
                self.LineInfo(
                    start=current_pos,
                    end=current_pos + len(line),
                    number=i + 1,
                    content=line,
                ))
            current_pos += len(line) + 1
        self.lines = tuple(lines)

    def get_codeinfo(self, start, end):
        """
        """
        lines = []
        start_line = end_line = None
        for line in self.lines:
            if not start_line and line.start <= start <= line.end:
                start_line = line
            if not end_line and line.start <= end <= line.end:
                end_line = line
            if start_line or end_line:
                lines.append(line)
            if start_line and end_line:
                break
        text = '\n'.join(l.content for l in lines)
        startpos = start - lines[0].start
        endpos = sum(len(l.content) + 1 for l in lines[:-1]) + (end - lines[-1].start) - 1
        return CodeInfo(
            text=text,
            startpos=startpos,
            endpos=endpos,
            line_numbers=tuple(l.number for l in lines),
            source=self.source,
        )

    @elements_to_values
    @add_codeinfo
    def dice(self, text, start, end, values, codeinfo):
        return elements.NewDice(*values, codeinfo=codeinfo)

    @elements_to_values
    @add_codeinfo
    def binary_op(self, text, start, end, values, codeinfo):
        left, op, right = values
        if not isinstance(op, elements.Operator):
            op = util.get_operator(op)
        if isinstance(left, (int, float)) and isinstance(right, (int, float)) \
                and op.value in constants.OPERATOR_MAP:
            return constants.OPERATOR_MAP[op.value](left, right)
        if isinstance(left, elements.StringLiteral) and isinstance(right, elements.StringLiteral):
            codeinfo = CodeInfo(
                text=text[left.codeinfo.startpos:right.codeinfo.endpos],
                startpos=left.codeinfo.startpos,
                endpos=right.codeinfo.endpos,
                lineno=left.codeinfo.lineno,
            )
            return elements.StringLiteral((left, right), codeinfo=codeinfo)
        return elements.BinaryOp(left, op, right, codeinfo=codeinfo)

    @elements_to_values
    @add_codeinfo
    def use_if(self, text, start, end, values, codeinfo):
        return elements.UseIf(*values, codeinfo=codeinfo)

    @add_codeinfo
    def basic_name(self, text, start, end, values, codeinfo):
        name = text[start:end]
        if name in elements.KEYWORDS:
            raise InvalidNameError(f'{name} is a keyword and cannot be used.', codeinfo=codeinfo)
        return name

    def int_(self, text, start, end, elements):
        return int(''.join(text[start:end]))

    def float_(self, text, start, end, elements):
        return float(''.join(text[start:end]))

    @add_codeinfo
    def string(self, text, start, end, values, codeinfo):
        return elements.StringLiteral(
            constants.ESCAPE_STR_PAT.sub(lambda m: constants.ESCAPE_MAP[m.group(1)],
                                         text[start + 1:end - 1]),
            codeinfo=codeinfo,
        )

    def special_entry(self, text, start, end, values):
        return elements.SpecialEntry(text[start:end])

    def special_accessor(self, text, start, end, values):
        return elements.SpecialAccessor(text[start:end])

    def special_ref(self, text, start, end, values):
        return elements.SpecialReference(text[start:end])

    @add_codeinfo
    def reference(self, text, start, end, values, codeinfo):
        value = text[start:end]
        if value in langref.KEYWORD_SET:
            return None
        return elements.Reference(value, codeinfo=codeinfo)

    def text(self, text, start, end, values):
        return text[start:end]

    def ignore(self, *args):
        return None

    @elements_to_values
    def overload_only_operator(self, text, start, end, values):
        if values:
            return elements.OverloadOnlyOperator(''.join(values))
        return elements.OverloadOnlyOperator(text[start:end])

    def one_sided_operator(self, text, start, end, values):
        return elements.OneSidedOperator(text[start:end])

    def two_sided_operator(self, text, start, end, values):
        return elements.TwoSidedOperator(text[start:end])

    @elements_to_values
    @add_codeinfo
    def negate(self, text, start, end, values, codeinfo):
        return util.negate(values[0], codeinfo=codeinfo, script=text)

    @elements_to_values
    @add_codeinfo
    def normal_modifier_body(self, text, start, end, values, codeinfo):
        params = body = ()
        if values and is_valid_iterable(values[0]):
            values = values[0]
        if values and isinstance(values[0], internal.ItemList):
            params = tuple(values.pop(0))
        if values:
            body = values[0]
            if not is_valid_iterable(body):
                body = (body,)
            else:
                body = util.flatten_tuple(body)
        return params, body

    @add_codeinfo
    def small_modifier_body(self, text, start, end, values, codeinfo):
        params, body = self.normal_modifier_body(text, start, end, values)
        return params, elements.Assignment(
            target=elements.SpecialReference.SUBJECT,
            value=body[0],
            codeinfo=codeinfo,
        )

    @elements_to_values
    @add_codeinfo
    def modifier_def(self, text, start, end, values, codeinfo):
        target, (params, body) = values
        if target == '!':
            target = elements.SpecialReference.NONE
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
    def first_modifier_call(self, text, start, end, values, codeinfo):
        target, op, call = values
        if op == ':':
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
    def modifier_call(self, text, start, end, values, codeinfo):
        if len(values) == 1:
            return elements.ModifierCall(modifier=values[0], args=(), codeinfo=codeinfo)
        return elements.ModifierCall(
            modifier=values[0],
            args=ensure_tuple(values[-1]),
            codeinfo=codeinfo,
        )

    @elements_to_values
    @add_codeinfo
    def modify(self, text, start, end, values, codeinfo):
        (subject, first_call), *other_calls = values
        calls = [first_call]
        if other_calls:
            if is_valid_iterable(other_calls[0]):
                calls += other_calls[0]
            else:
                calls.append(other_calls[0])
        return elements.Modify(subject=subject, modifiers=tuple(calls), codeinfo=codeinfo)

    @elements_to_values
    def param_list(self, text, start, end, values):
        return internal.ItemList(p.value for p in util.flatten_tuple(values))

    @elements_to_values
    def arg_list(self, text, start, end, values):
        return util.flatten_tuple(values)

    @elements_to_values
    @add_codeinfo
    def left_op_overload(self, text, start, end, values, codeinfo):
        return elements.OverloadOperator(operator=elements.TwoSidedOperator(values[0]),
                                         side=elements.OperationSide.LEFT,
                                         codeinfo=codeinfo)

    @elements_to_values
    @add_codeinfo
    def right_op_overload(self, text, start, end, values, codeinfo):
        return elements.OverloadOperator(operator=elements.TwoSidedOperator(values[0]),
                                         side=elements.OperationSide.RIGHT,
                                         codeinfo=codeinfo)

    @elements_to_values
    @add_codeinfo
    def one_sided_op_overload(self, text, start, end, values, codeinfo):
        value = values[0]
        if not isinstance(value, str):
            value = ''.join(value)
        return elements.OverloadOperator(operator=elements.OneSidedOperator(value),
                                         side=elements.OperationSide.NA,
                                         codeinfo=codeinfo)

    @elements_to_values
    @add_codeinfo
    def raw_accessor(self, text, start, end, values, codeinfo):
        return elements.RawAccessor(values[0], codeinfo=codeinfo)

    #TODO implement expand
    @elements_to_values
    @add_codeinfo
    def access(self, text, start, end, values, codeinfo):
        accessing = values[0]
        accessors = ensure_tuple(values[-1])
        current_accessors = []
        for accessor in accessors:
            if accessor == elements.SpecialAccessor.EVERY:
                if current_accessors:
                    accessing = elements.Expand(
                        elements.Access(accessing=accessing,
                                        accessors=tuple(current_accessors),
                                        codeinfo=codeinfo),
                        codeinfo=codeinfo,
                    )
                    current_accessors = []
                else:
                    accessing = elements.Expand(accessing, codeinfo=codeinfo)
            else:
                current_accessors.append(accessor)
        if current_accessors:
            accessing = elements.Access(
                accessing=accessing,
                accessors=tuple(current_accessors),
                codeinfo=codeinfo,
            )
        return accessing

    @elements_to_values
    @add_codeinfo
    def reduce(self, text, start, end, values, codeinfo):
        value = values[0]
        if value == '*':
            value = elements.SpecialReference.ALL
        return elements.Reduce(value, codeinfo=codeinfo)

    @elements_to_values
    @add_codeinfo
    def modify_and_assign(self, text, start, end, values, codeinfo):
        return (elements.Assignment(
            target=values[0],
            value=elements.Modify(subject=values[0],
                                  modifiers=util.flatten_tuple(values[1:]),
                                  codeinfo=codeinfo),
            codeinfo=codeinfo,
        ))

    @elements_to_values
    @add_codeinfo
    def assignment(self, text, start, end, values, codeinfo):
        target, op, value = values
        if len(op) > 1:
            value = elements.BinaryOp(left=target,
                                      op=util.get_operator(op[:-1]),
                                      right=value,
                                      codeinfo=codeinfo)
        if target == value:
            return None
        return elements.Assignment(target=target, value=value, codeinfo=codeinfo)

    @elements_to_values
    @add_codeinfo
    def reduce_and_assign(self, text, start, end, values, codeinfo):
        return elements.Assignment(target=values[0],
                                   value=elements.Reduce(values[0], codeinfo=codeinfo),
                                   codeinfo=codeinfo)

    @add_codeinfo
    def leave(self, text, start, end, values, codeinfo):
        return elements.Leave(codeinfo=codeinfo)

    @elements_to_values
    @add_codeinfo
    def otherwise(self, text, start, end, values, codeinfo):
        return internal.Otherwise(values[-1], codeinfo=codeinfo)

    @elements_to_values
    @add_codeinfo
    def fill(self, text, start, end, values, codeinfo):
        return elements.Fill(*values, codeinfo=codeinfo)

    @add_codeinfo
    def empty_roll(self, text, start, end, values, codeinfo):
        return elements.NewRoll((), codeinfo=codeinfo)

    @elements_to_values
    @add_codeinfo
    def roll_def(self, text, start, end, values, codeinfo):
        if len(values) == 1:
            if not is_valid_iterable(values[0]):
                return elements.NewRoll(tuple(values), codeinfo=codeinfo)
            values = values[0]
        return elements.NewRoll(util.flatten_tuple(tuple(values)), codeinfo=codeinfo)

    @elements_to_values
    @add_codeinfo
    def new_bag(self, text, start, end, values, codeinfo):
        if not values:
            return elements.NewBag((), codeinfo=codeinfo)
        return elements.NewBag(util.flatten_tuple(values), codeinfo=codeinfo)

    @elements_to_values
    @add_codeinfo
    def clear(self, text, start, end, values, codeinfo):
        return elements.ClearValue(values[0], codeinfo=codeinfo)

    @elements_to_values
    @add_codeinfo
    def load_from_into(self, text, start, end, values, codeinfo):
        to_load, load_from, *into = values
        if into:
            into = into[0]
        else:
            into = elements.SpecialReference.LOCAL
        if to_load == '*':
            to_load = elements.SpecialReference.ALL
        elif is_valid_iterable(to_load):
            to_load = util.flatten_tuple(to_load)
        else:
            to_load = ensure_tuple(to_load)
        return elements.Load(
            to_load=to_load,
            load_from=load_from,
            into=into,
            codeinfo=codeinfo,
        )

    @elements_to_values
    @add_codeinfo
    def load_from(self, text, start, end, values, codeinfo):
        to_load, load_from = values
        if to_load == '*':
            to_load = elements.SpecialReference.ALL
        elif is_valid_iterable(to_load):
            to_load = util.flatten_tuple(to_load)
        else:
            to_load = ensure_tuple(to_load)
        return elements.Load(
            to_load=to_load,
            load_from=load_from,
            into=elements.SpecialReference.LOCAL,
            codeinfo=codeinfo,
        )

    @elements_to_values
    @add_codeinfo
    def load_into(self, text, start, end, values, codeinfo):
        things_to_load_from, into = values
        if is_valid_iterable(things_to_load_from):
            things_to_load_from = util.flatten_tuple(things_to_load_from)
        items = []
        for load_from in ensure_tuple(things_to_load_from):
            items.append(
                elements.Load(
                    to_load=elements.SpecialReference.ALL,
                    load_from=load_from,
                    into=into,
                    codeinfo=codeinfo,
                ))
        return tuple(items)

    @elements_to_values
    @add_codeinfo
    def load(self, text, start, end, values, codeinfo):
        if is_valid_iterable(values[0]):
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

    @elements_to_values
    @add_codeinfo
    def unless(self, text, start, end, values, codeinfo):
        preeval_res = preevaluate_predicate(values[0])
        if preeval_res is DeferEvaluation:
            return internal.Unless(*values, codeinfo=codeinfo)
        if preeval_res:
            return internal.Wrapper('unless', values[-1], codeinfo=codeinfo)
        return internal.UseOtherwise

    @elements_to_values
    @add_codeinfo
    def if_(self, text, start, end, values, codeinfo):
        preeval_res = preevaluate_predicate(values[0])
        if preeval_res is DeferEvaluation:
            return internal.If(*values, codeinfo=codeinfo)
        if preeval_res:
            return internal.Wrapper('if', values[-1], codeinfo=codeinfo)
        return internal.UseOtherwise

    @elements_to_values
    @add_codeinfo
    def predicated_statement(self, text, start, end, values, codeinfo):
        return internal.PredicatedStatement(*values, codeinfo=codeinfo)

    @staticmethod
    def _create_if_then_element(predicated, otherwise, codeinfo):
        if predicated is internal.UseOtherwise:
            return otherwise
        if isinstance(predicated, internal.Wrapper):
            return predicated.value
        if codeinfo == 'from-predicated':
            codeinfo = predicated.codeinfo
        return elements.IfThen(
            predicate=predicated.predicate,
            then=ensure_tuple(predicated.statement),
            otherwise=ensure_tuple(otherwise),
            codeinfo=codeinfo,
        )

    @elements_to_values
    @add_codeinfo
    def if_stmt(self, text, start, end, values, codeinfo):
        if_ = values.pop(0)
        if not values:
            return self._create_if_then_element(if_, (), codeinfo)
        otherwise = values.pop(-1)
        unlesses = ()
        if isinstance(otherwise, internal.Otherwise):
            if not values:
                return self._create_if_then_element(if_, otherwise.value, codeinfo)
            unlesses = ensure_tuple(values[0])
            otherwise = otherwise.value
        else:
            unlesses = ensure_tuple(otherwise)
            otherwise = ()
        stmt = self._create_if_then_element(if_, otherwise, codeinfo)
        for unless in reversed(unlesses):
            stmt = self._create_if_then_element(unless, stmt, 'from-predicated')
        return stmt

    # pylint: disable=protected-access
    @elements_to_values
    @add_codeinfo
    def restart(self, text, start, end, values, codeinfo):
        location_specifier = elements.RestartLocationSpecifier(values[0])
        target = elements.SpecialReference.NONE
        with suppress(IndexError):
            target = values[1]
        if isinstance(target, elements.Reference) \
                and not isinstance(target, elements.SpecialReference):
            target = target.value
        return elements.Restart(
            location_specifier=location_specifier,
            target=target,
            codeinfo=codeinfo,
        )

    @elements_to_values
    @add_codeinfo
    def loop_name(self, text, start, end, values, codeinfo):
        return internal.LoopName(values[0].value, codeinfo=codeinfo)

    @elements_to_values
    @add_codeinfo
    def loop_body(self, text, start, end, values, codeinfo):
        return internal.LoopBody(values[0], codeinfo=codeinfo)

    @elements_to_values
    @add_codeinfo
    def until_do(self, text, start, end, values, codeinfo):
        name = until = do = otherwise = None
        if isinstance(values[0], internal.LoopName):
            name = values.pop(0)[0]
        until = values.pop(0)
        do = values.pop(0)[0]
        if values and isinstance(values[-1], internal.Otherwise):
            otherwise = values.pop(-1).value
        if values:
            for except_when in ensure_tuple(values[0]):
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
    def for_every(self, text, start, end, values, codeinfo):
        loop_name = None
        if isinstance(values[0], internal.LoopName):
            loop_name = values.pop(0)[0]
        item_name = values[0]
        if isinstance(item_name, elements.Reference):
            item_name = item_name.value
        return elements.ForEvery(
            name=loop_name,
            item_name=item_name,
            iterable=values[1],
            do=ensure_tuple(values[-1][0]),
            codeinfo=codeinfo,
        )

    @elements_to_values
    @add_codeinfo
    def block(self, text, start, end, values, codeinfo):
        if is_valid_iterable(values[0]):
            return util.flatten_tuple(values[0])
        return values[0]

    def empty_block(self, *args):
        return ()

    @elements_to_values
    @add_codeinfo
    def but_if(self, text, start, end, values, codeinfo):
        predicate, statement = values
        if predicate == '*':
            predicate = elements.SpecialReference.ALL
        return elements.ButIf(predicate, statement, codeinfo=codeinfo)

    @elements_to_values
    @add_codeinfo
    def always(self, text, start, end, values, codeinfo):
        return internal.Always(values[0])

    @elements_to_values
    @add_codeinfo
    def attempt(self, text, start, end, values, codeinfo):
        attempt, *remainder = values
        if not remainder:
            return elements.Attempt(
                attempt=attempt,
                buts=(),
                always=None,
                codeinfo=codeinfo,
            )
        if remainder:
            *buts, always = remainder
        if not isinstance(always, internal.Always):
            buts = tuple((*buts, always))
            always = None
        else:
            always = always[0]
        if buts and is_valid_iterable(buts[0]):
            buts = buts[0]
        return elements.Attempt(
            attempt=attempt,
            buts=buts,
            always=always,
            codeinfo=codeinfo,
        )

    @elements_to_values
    @add_codeinfo
    def oops(self, text, start, end, values, codeinfo):
        return elements.Oops(values[0], codeinfo=codeinfo)

    @elements_to_values
    def statements(self, text, start, end, values):
        return values
