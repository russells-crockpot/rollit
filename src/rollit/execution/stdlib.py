"""
"""

from ..ast.elements import Dice
from ..exceptions import RollitTypeError
from ..internal_objects import PythonBasedModifier, Bag, Roll

__all__ = [
    'the_library',
]


@PythonBasedModifier
def _print(*args, subject, context):
    print(subject, *args)


@PythonBasedModifier
def _top(*args, subject, context):
    if not args:
        num = 1
    else:
        num = args[0]
    if isinstance(subject, Dice):
        subject = context.reduce(subject)
    if not isinstance(subject, Roll):
        raise RollitTypeError()
    return Roll(sorted(subject, reverse=True)[0:num])


@PythonBasedModifier
def _bottom(*args, subject, context):
    if not args:
        num = 1
    else:
        num = args[0]
    if isinstance(subject, Dice):
        subject = context.reduce(subject)
    if not isinstance(subject, Roll):
        raise RollitTypeError()
    return Roll(sorted(subject)[0:num])


the_library = Bag({
    'print': _print,
    'top': _top,
    'bottom': _bottom,
})
