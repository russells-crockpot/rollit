#pylint: disable=too-many-function-args
"""
"""
from contextlib import suppress

from ..ast import elements, constants
from ..exceptions import RollItTypeError
from ..internal_objects import Roll, Bag, OopsException
from ..language_ref import OPERATORS

__all__ = ()


@elements.Reduce.evaluator
def _(self, context):
    return context.reduce(context(self.value))


@elements.Assignment.evaluator
def _(self, context):
    if isinstance(self.target, str):
        context[self.target] = context(self.value)
    else:
        target = context.access_obj(self.target.accessing, self.target.accessors[:-1])
        target[self.target.accessors[-1]] = context(self.value)


@elements.Access.evaluator
def _(self, context):
    if isinstance(self.accessing, str):
        current_item = context[self.accessing]
    else:
        current_item = context(self.accessing)
    return context.access(current_item, *self.accessors)


@elements.Enlarge.evaluator
def _(self, context):
    return Roll(context(self.value) for _ in range(context(self.size)))


@elements.Dice.evaluator
def _(self, context):
    return self


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
    return Bag()


# Because these objects are predicated, we can just have their children be evaluated
@elements.ButIf.evaluator
@elements.UseIf.evaluator
@elements.IfThen.evaluator
def _(self, context):
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
                raise RollItTypeError()
    else:
        del context[to_clear]


@elements.Oops.evaluator
def _(self, context):
    raise OopsException(context(self.value))


@elements.Attempt.evaluator
def _(self, context):
    raise NotImplementedError()


@elements.Leave.evaluator
def _(self, context):
    raise NotImplementedError()


@elements.Modify.evaluator
def _(self, context):
    raise NotImplementedError()


@elements.Load.evaluator
def _(self, context):
    raise NotImplementedError()


@elements.ForEvery.evaluator
def _(self, context):
    raise NotImplementedError()


@elements.ModifierDef.evaluator
def _(self, context):
    raise NotImplementedError()


@elements.Restart.evaluator
def _(self, context):
    raise NotImplementedError()


@elements.UntilDo.evaluator
def _(self, context):
    raise NotImplementedError()


@elements.Dice.reducer
def _(self, context):
    number_of_dice = context(self.number_of_dice)
    return Roll([context.roll(context(self.sides)) for _ in range(number_of_dice)])
