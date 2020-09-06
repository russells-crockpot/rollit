#pylint: disable=too-many-function-args
"""
"""
from contextlib import suppress, nullcontext

from ..ast import elements, constants
from ..exceptions import RollitTypeError
from .objects import Roll, Bag, OopsException, RestartException, LeaveException, \
        RollitBasedModifier, Dice
from ..langref import OPERATORS
from ..util import is_valid_iterable

__all__ = ()


def _access_all_but_last(access, context):
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


@elements.Reduce.reducer
@elements.Reduce.evaluator
def _(self, context):
    with context.now_access(context.scope):
        return context.reduce(context(self.value))


@elements.RawAccessor.evaluator
def _(self, context):
    with context.now_access(context.scope):
        return context(self.value)


@elements.Assignment.evaluator
def _(self, context):
    cm = nullcontext()
    target = self.target
    if isinstance(target, elements.Access):
        accessing, target = _access_all_but_last(self.target, context)
        cm = context.now_access(accessing)
    if isinstance(target, elements.Reference):
        target = target.value
    with cm:
        if isinstance(target, elements.RawAccessor):
            context.accessing.raw_set(context(target), context(self.value))
        elif isinstance(target, (elements.SpecialAccessor, elements.SpecialEntry)):
            context[target] = context(self.value)
        else:
            context[context(target)] = context(self.value)


@elements.Access.evaluator
def _(self, context):
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
def _(self, context):
    to_clear = self.value
    cm = nullcontext()
    if isinstance(to_clear, elements.Access):
        base, to_clear = _access_all_but_last(to_clear, context)
        if isinstance(to_clear, elements.Reduce):
            to_clear = context.reduce(to_clear)
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
def _(self, context):
    size = 1 if self.size is None else self.size
    return Roll(context(self.value) for _ in range(context(size)))


@elements.DiceNode.evaluator
def _(self, context):
    num_dice, sides, *_ = self
    if isinstance(num_dice, elements.Reduce):
        num_dice = context(num_dice)
    if isinstance(sides, elements.Reduce):
        sides = context(sides)
    return Dice(num_dice, sides)


@elements.Negation.evaluator
def _(self, context):
    return not context(self.value)


@elements.BinaryOp.evaluator
def _(self, context):
    left = context(self.left)
    right = context(self.right)
    #FIXME handle string concatination and other operators
    # pylint: disable=no-member
    if self.op in OPERATORS.math:
        left = context.full_reduce(left)
        right = context.full_reduce(right)
    return constants.OPERATOR_MAP[self.op](left, right)


@elements.NewBag.evaluator
def _(self, context):
    bag = Bag(context)
    with context.now_access(bag):
        for stmt in self.value:
            context(stmt)
    # pylint: disable=protected-access
    bag._special_entries.on_create()
    return bag


@elements.IfThen.evaluator
def _(self, context):
    if context(self.predicate):
        for stmt in self.then:
            context(stmt)
    else:
        for stmt in self.otherwise:
            context(stmt)


@elements.UseIf.evaluator
def _(self, context):
    if context(self.predicate):
        return context(self.use)
    return context(self.otherwise)


@elements.ButIf.evaluator
def _(self, context):
    if context(self.predicate):
        context(self.statement)


@elements.StringLiteral.evaluator
@elements.StringLiteral.reducer
def _(self, context):
    return self.value


@elements.Reference.evaluator
def _(self, context):
    return context[self.value]


@elements.Oops.evaluator
def _(self, context):
    raise OopsException(context(self.value))


@elements.Leave.evaluator
def _(self, context):
    raise LeaveException()


@elements.Modify.evaluator
def _(self, context):
    with context.new_scope(isolate=True):
        with context.use_subject(context(self.subject)):
            for name, args, _ in self.modifiers:
                context(name).call(*(context(a) for a in args), context=context)
            return context.scope.subject


@elements.ModifierDef.evaluator
def _(self, context):
    with context.new_scope(isolate=True) as scope:
        modifier = RollitBasedModifier(self, scope)
    if self.target in (None, elements.SpecialReference.NONE):
        return modifier
    context(elements.Assignment(self.target, modifier, codeinfo=self.codeinfo))
    return None


@elements.Attempt.evaluator
def _(self, context):
    try:
        context(self.attempt)
    except OopsException as e:
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
def _(self, context):
    raise NotImplementedError()


@elements.ForEvery.evaluator
def _(self, context):
    raise NotImplementedError()


@elements.Restart.evaluator
def _(self, context):
    raise RestartException(*self)


@elements.UntilDo.evaluator
def _(self, context):

    def _before():
        if context(self.until):
            if self.otherwise:
                context(self.otherwise)
            return True
        return False

    with context.new_scope():
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
            except RestartException as e:
                if e.name and e.name not in (elements.SpecialReference.NONE, self.name):
                    raise
                if e.location_specifier == elements.RestartLocationSpecifier.AT:
                    ignore_predicate = True
                elif e.location_specifier == elements.RestartLocationSpecifier.BEFORE:
                    if _before():
                        return
                elif e.location_specifier == elements.RestartLocationSpecifier.AFTER:
                    return


@elements.Reference.reducer
def _(self, context):
    return context.reduce(context(self))
