"""
"""

from ..exceptions import RollitTypeError
from .objects import PythonBasedModifier, PythonBasedLibrary, Roll, Dice, Bag

__all__ = [
    'stdlib',
]


@PythonBasedModifier
# pylint: disable=useless-return
def _print(*args, subject, context):
    print(subject, *args)
    return None


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


@PythonBasedModifier
# pylint: disable=protected-access
def _in_scope(*args, subject, context):
    scopes = []
    scope = context.scope
    while scope.parent:
        scopes.append(scope._variables._entries)
        scope = scope.parent
    scopes.append(scope._variables._entries)
    entries = {}
    for scope in reversed(scopes):
        entries.update(scope)
    bag = Bag(context)
    bag._entries = entries
    return bag


@PythonBasedModifier
# pylint: disable=protected-access
def _names_in_scope(*args, subject, context):
    names = set()
    scope = context.scope
    while scope.parent:
        names |= set(scope.variable_names())
        scope = scope.parent
    names |= set(scope.variable_names())
    names = Roll(names)
    names.sort()
    return names


stdlib = PythonBasedLibrary({
    'print': _print,
    'top': _top,
    'bottom': _bottom,
    'in_scope': _in_scope,
    'names_in_scope': _names_in_scope,
})
