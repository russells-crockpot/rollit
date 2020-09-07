# pylint: disable=protected-access
"""
"""
import os as os_
import sys
from contextlib import suppress
from types import MappingProxyType

from .. import rli
from ..exceptions import RollitTypeError
from ..objects import Roll, Dice, Bag

__all__ = [
    'rootlib',
    'BUILTIN_LIBRARIES',
]

rootlib = rli.PythonBasedLibrary('~')
""" """


@rootlib.modifier('print')
# pylint: disable=useless-return
def _(*args, subject, context):
    print(subject, *args)
    return None


@rootlib.modifier('top')
def _(*args, subject, context):
    if not args:
        num = 1
    else:
        num = args[0]
    if isinstance(subject, Dice):
        subject = context.reduce(subject)
    if not isinstance(subject, Roll):
        raise RollitTypeError()
    return Roll(sorted(subject, reverse=True)[0:num])


@rootlib.modifier('bottom')
def _(*args, subject, context):
    if not args:
        num = 1
    else:
        num = args[0]
    if isinstance(subject, Dice):
        subject = context.reduce(subject)
    if not isinstance(subject, Roll):
        raise RollitTypeError()
    return Roll(sorted(subject)[0:num])


runtime = rli.PythonBasedLibrary('runtime')
"""
"""


@runtime.modifier('loops')
def _(*args, subject, context):
    return Roll(context.scope.loops)


@runtime.modifier('scope_entries')
def _(*args, subject, context):
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


@runtime.modifier('names_in_scope')
def _(*args, subject, context):
    names = set()
    scope = context.scope
    while scope.parent:
        names |= set(scope.variable_names())
        scope = scope.parent
    names |= set(scope.variable_names())
    names = Roll(names)
    names.sort()
    return names


@runtime.on_access
def _(name, lib, context):
    if name == 'cwd':
        return os_.getcwd()
    return lib.raw_get(name)


os = rli.PythonBasedLibrary('os')


@os.entry('name')
def _():
    if sys.platform.startswith('linux'):
        return 'linux'
    if sys.platform.startswith('win'):
        return 'windows'
    if sys.platform.startswith('cygwin'):
        return 'cygwin'
    if sys.platform.startswith('darwin'):
        return 'macos'
    return sys.platform.rstrip('0123456789. -_')


os.envvars = rli.BagPlaceholder()


@os.envvars.on_access
def _(name, subject, context):
    with suppress(KeyError):
        return os_.environ[context(name)]
    return None


@os.envvars.on_set
def _(name, value, subject, context):
    os_.environ[context(name)] = str(context(value))


BUILTIN_LIBRARIES = MappingProxyType({
    rootlib.name: rootlib,
    runtime.name: runtime,
    os.name: os,
})
