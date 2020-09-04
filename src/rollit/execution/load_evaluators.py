#pylint: disable=too-many-function-args
"""
"""
from contextlib import suppress

from ..ast import elements, constants, is_valid_iterable
from ..exceptions import RollitTypeError
from .objects import Roll, Bag, OopsException, RestartException, LeaveException, \
        RollitBasedModifier, Dice
from ..langref import OPERATORS

__all__ = ()


@elements.Reduce.reducer
@elements.Reduce.evaluator
def _(self, context):
    return context.reduce(context(self.value))


@elements.Assignment.evaluator
def _(self, context):
    if isinstance(self.target, elements.Reference):
        context[self.target.value] = context(self.value)
    else:
        if len(self.target.accessors) == 1:
            target = context(self.target.accessing)
        else:
            target = context(
                elements.Access(self.target.accessing,
                                self.target.accessors[:-1],
                                codeinfo=self.target.codeinfo))
        final_accessor = self.target.accessors[-1]
        if isinstance(final_accessor, elements.Reference):
            final_accessor = final_accessor.value
        else:
            final_accessor = context.full_reduce(final_accessor)
        target[final_accessor] = context(self.value)


@elements.Access.evaluator
def _(self, context):
    accessing = context(self.accessing)
    for accessor in self.accessors:
        if isinstance(accessor, elements.Reduce):
            accessing = accessing[context(accessor)]
        else:
            with context.now_access(accessing):
                accessing = context(accessor)
    return accessing


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
    parent = context(self.parent)
    bag = Bag(parent=parent, isolate=self.isolate)
    if self.statements:
        with context.now_access(bag):
            for stmt in self.statements:
                context(stmt)
    return bag


# Because these objects are predicated, we can just have their children be evaluated
@elements.ButIf.evaluator
@elements.UseIf.evaluator
@elements.IfThen.evaluator
def _(self, context):
    #TODO
    return context.evaluate_children(self)


@elements.ClearValue.evaluator
def _(self, context):
    to_clear = self.value
    if isinstance(to_clear, elements.Access):
        #TODO
        base = context(
            elements.Access(to_clear.accessing, to_clear.accessors[:-1], codeinfo=self.codeinfo))
        last = context.get_accessor_value(to_clear.accessors[-1])
        with suppress(LookupError):
            try:
                del base[last]
            except TypeError:
                raise RollitTypeError()
    else:
        del context[to_clear]


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
    context.scope.subject = context(self.subject)
    for name, args, _ in self.modifiers:
        modifier = context(name)
        try:
            modifier.modify(*(context(a) for a in args), context=context)
        except LeaveException:
            continue
    return context.scope.subject


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


@elements.ModifierDef.evaluator
def _(self, context):
    modifier = RollitBasedModifier(self, context.scope)
    if self.target in (None, elements.SpecialReference.NONE):
        return modifier
    with context.now_access(context.scope.parent):
        context(elements.Assignment(self.target, modifier, codeinfo=self.codeinfo))
    return None


@elements.UntilDo.evaluator
def _(self, context):

    def _before():
        if context(self.until):
            if self.otherwise:
                context(self.otherwise)
            return True
        return False

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
