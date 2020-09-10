#pylint: disable=too-many-function-args,missing-docstring
from collections import namedtuple
from contextlib import suppress, nullcontext

from .base import context
from .. import objects
from ..ast import elements, constants
from ..exceptions import RollitTypeError, NoSuchLoopError, RollitReferenceError, CannotReduceError
from ..util import is_valid_iterable

__all__ = ()


def _access_all_but_last(access):
    final_accessor = access.accessors[-1]
    if isinstance(final_accessor, elements.Reduce):
        final_accessor = context(final_accessor)
    # pylint: disable=unexpected-keyword-arg
    return context(
        elements.Access(
            accessing=access.accessing,
            accessors=access.accessors[:-1],
            codeinfo=access.codeinfo,
        )), final_accessor


@elements.Reduce.evaluator
def _(self):
    with context.now_access(context.scope):
        to_reduce = context(self.value)
        if not isinstance(to_reduce, objects.InternalObject):
            return to_reduce
        rval = to_reduce.operate_on(elements.OverloadOnlyOperator.REDUCE)
        if rval is NotImplemented:
            raise CannotReduceError(self.value)
        return rval


@elements.RawAccessor.evaluator
def _(self):
    with context.now_access(context.scope):
        return context(self.value)


@elements.Assignment.evaluator
def _(self):
    cm = nullcontext()
    target = self.target
    if isinstance(target, elements.Access):
        accessing, target = _access_all_but_last(self.target)
        cm = context.now_access(accessing)
    if isinstance(target, elements.Reference):
        target = target.value
    with cm:
        if isinstance(target, elements.RawAccessor):
            context.accessing.raw_set(context(target), context(self.value))
        elif isinstance(target, elements.OverloadOperator):
            if not isinstance(context.accessing, objects.InternalObject):
                raise RollitTypeError(self)
            context.accessing.override_operator(target.operator, target.side, context(self.value))
        elif isinstance(target, (elements.SpecialAccessor, elements.SpecialEntry)):
            context[target] = context(self.value)
        else:
            context[context(target)] = context(self.value)


@elements.Access.evaluator
def _(self):
    accessing = context(self.accessing)
    for accessor in self.accessors:
        with context.now_access(accessing, allow_scope_access=False):
            if isinstance(accessor, elements.Reduce):
                accessing = accessing[context(accessor)]
            elif isinstance(accessor, elements.RawAccessor):
                accessing = accessing.raw_get(context(accessor))
            else:
                accessing = context(accessor)
    return accessing


@elements.ClearValue.evaluator
def _(self):
    to_clear = self.value
    cm = nullcontext()
    if isinstance(to_clear, elements.Access):
        base, to_clear = _access_all_but_last(to_clear)
        if isinstance(to_clear, elements.Reduce):
            to_clear = context(to_clear)
        cm = context.now_access(base, allow_scope_access=False)
    if isinstance(to_clear, elements.Reference):
        to_clear = to_clear.value
    with cm:
        with suppress(LookupError):
            try:
                if isinstance(to_clear, elements.RawAccessor):
                    context.accessing.raw_clear(context(to_clear))
                else:
                    del context[to_clear]
            except TypeError:
                raise RollitTypeError()


@elements.Enlarge.evaluator
def _(self):
    size = 1 if self.size is None else self.size
    return objects.Roll(context(self.value) for _ in range(context(size)))


@elements.DiceNode.evaluator
def _(self):
    num_dice, sides, *_ = self
    if isinstance(num_dice, elements.Reduce):
        num_dice = context(num_dice)
    if isinstance(sides, elements.Reduce):
        sides = context(sides)
    return objects.Dice(num_dice, sides)


@elements.Negation.evaluator
def _(self):
    return not context(self.value)


@elements.BinaryOp.evaluator
def _(self):
    left = context(self.left)
    right = context(self.right)
    rval = NotImplemented
    if isinstance(left, objects.InternalObject):
        rval = left.operate_on(self.op, elements.OperationSide.LEFT, right)
    if rval is NotImplemented and isinstance(right, objects.InternalObject):
        rval = right.operate_on(self.op, elements.OperationSide.RIGHT, left)
    if isinstance(rval, elements.ModelElement):
        return context(rval)
    if isinstance(rval, (int, str, float, objects.InternalObject)):
        return rval
    if rval is NotImplemented:
        try:
            return constants.OPERATOR_MAP[self.op.value](left, right)
        except TypeError:
            raise RollitTypeError()
    raise RollitTypeError()


@elements.NewBag.evaluator
def _(self):
    bag = objects.Bag()
    with context.now_access(bag):
        for stmt in self.value:
            context(stmt)
    # pylint: disable=protected-access
    bag._special_entries.on_create()
    return bag


@elements.IfThen.evaluator
def _(self):
    if context(self.predicate):
        for stmt in self.then:
            context(stmt)
    else:
        for stmt in self.otherwise:
            context(stmt)


@elements.UseIf.evaluator
def _(self):
    if context(self.predicate):
        return context(self.use)
    return context(self.otherwise)


@elements.ButIf.evaluator
def _(self):
    if context(self.predicate):
        context(self.statement)


@elements.StringLiteral.evaluator
def _(self):
    return self.value


@elements.Reference.evaluator
def _(self):
    return context[self.value]


@elements.Oops.evaluator
def _(self):
    raise objects.OopsException(context(self.value))


@elements.Leave.evaluator
def _(self):
    raise objects.LeaveException()


@elements.Modify.evaluator
def _(self):
    with context.new_scope(isolate=True):
        with context.use_subject(context(self.subject)):
            for name, args, _ in self.modifiers:
                context(name).call(*(context(a) for a in args))
            return context.scope.subject


@elements.ModifierDef.evaluator
def _(self):
    with context.new_scope(isolate=True) as scope:
        modifier = objects.RollitBasedModifier(self, scope)
    if self.target in (None, elements.SpecialReference.NONE):
        return modifier
    context(elements.Assignment(self.target, modifier, codeinfo=self.codeinfo))
    return None


@elements.Attempt.evaluator
def _(self):
    try:
        context(self.attempt)
    except objects.OopsException as e:
        with context.new_scope(isolate=True, error=context(e.value)):
            for but in self.buts or ():
                if but.predicate == elements.SpecialReference.ALL or context(but.predicate):
                    context(but.statement)
                    return
            raise
    finally:
        if self.always:
            context(self.always)


@elements.Load.evaluator
def _(self):
    try:
        load_from = context(self.load_from)
    except RollitReferenceError:
        load_from = context.get_library(self.load_from.value)
    try:
        load_into = context(self.into)
    except RollitReferenceError:
        load_into = objects.Bag()
        context[self.into.value] = load_into
    if self.to_load == elements.SpecialReference.ALL:
        load_into.load(load_from)
    else:
        with context.now_access(load_into):
            for ref in self.to_load:
                context(elements.Assignment(ref, load_from[ref.value], codeinfo=ref.codeinfo))


@elements.Restart.evaluator
def _(self):
    raise objects.RestartException(*self)


class _SupressOn(namedtuple('_SupressOnBase', ('name', 'location_specifier'))):

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        if exc and isinstance(exc, objects.RestartException):
            if exc.name in (elements.SpecialReference.NONE, self.name):
                return self.location_specifier == exc.location_specifier
            if exc.name == elements.SpecialReference.PARENT:
                exc.name = elements.SpecialReference.NONE
                raise exc from None
            if exc.name not in context.scope.loops:
                raise NoSuchLoopError(exc.name)
        return False


@elements.ForEvery.evaluator
def _(self):
    with _SupressOn(self.name, elements.RestartLocationSpecifier.AFTER):
        while True:
            with _SupressOn(self.name, elements.RestartLocationSpecifier.BEFORE):
                with context.new_scope() as scope:
                    if self.name:
                        scope.add_loop(self.name)
                    source = context(self.iterable)
                    iterable = source.operate_on(elements.OverloadOnlyOperator.ITERATE)
                    if iterable is NotImplemented:
                        raise RollitTypeError(f'Only bags and rolls are iterable. Got: {source}')
                    for item in iterable:
                        scope[self.item_name] = item
                        with _SupressOn(self.name, elements.RestartLocationSpecifier.AT):
                            for stmt in self.do:
                                context(stmt)
                    return


@elements.UntilDo.evaluator
def _(self):

    def _before():
        if context(self.until):
            if self.otherwise:
                context(self.otherwise)
            return True
        return False

    with context.new_scope() as scope:
        if self.name:
            scope.add_loop(self.name)
        if _before():
            return
        do = self.do
        if not is_valid_iterable(do):
            do = (do,)
        ignore_predicate = True
        while ignore_predicate or not context(self.until):
            ignore_predicate = False
            try:
                for stmt in do:
                    context(stmt)
            except objects.RestartException as e:
                if e.name and e.name not in (elements.SpecialReference.NONE, self.name):
                    if e.name not in context.scope.loops:
                        raise NoSuchLoopError(e.name)
                    raise
                if e.location_specifier == elements.RestartLocationSpecifier.AT:
                    ignore_predicate = True
                elif e.location_specifier == elements.RestartLocationSpecifier.BEFORE:
                    if _before():
                        return
                elif e.location_specifier == elements.RestartLocationSpecifier.AFTER:
                    return


@elements.SpecialReference.evaluator
def _(self):
    if self.name == 'NONE':
        return None
    return context[self.value]


@elements.SpecialAccessor.evaluator
@elements.SpecialEntry.evaluator
def _(self):
    return context[self]
