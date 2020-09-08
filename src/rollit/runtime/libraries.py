# pylint: disable=protected-access, too-complex, using-constant-test
"""
"""
import math
import os as os_
import sys
from contextlib import suppress
from types import MappingProxyType

from .. import rli
from ..ast import elements
from ..exceptions import RollitTypeError
from ..objects import Roll, Dice, Bag

__all__ = [
    'rootlib',
    'os',
    'maths',
    'bags',
    'rolls',
    'strings',
    'loading',
    'BUILTIN_LIBRARIES',
]
#########################################################
# Note: The contents of each library is in a ``if True``
# block because it makes folding code easier and the code
# in general look cleaner/more organized.
#########################################################

############## rootlib ##############

rootlib = rli.PythonBasedLibrary('~')
""" """

if True:

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


############## runtime ##############
runtime = rli.PythonBasedLibrary('runtime')
"""
"""

if True:

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


############## os ##############
os = rli.PythonBasedLibrary('os')
"""
"""

if True:

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


############## io ##############
io = rli.PythonBasedLibrary('os')
"""
"""
if True:
    io.File = rli.BagPlaceholder()

    @io.File.modifier('create')
    def _(filename, subject, context):
        bag = Bag(context)
        bag['name'] = filename
        bag[elements.SpecialEntry.PARENT] = subject
        return bag

    @io.File.modifier('exists')
    def _(*, subject, context):
        return os_.path.exists(subject['name'])


############## maths ##############
maths = rli.PythonBasedLibrary('maths')
"""Yes, it's called ``maths`` and not ``math``. No I'm not British, but I like the way maths sounds
better (also, everyone uses ``math``; it's boring).
"""

if True:
    maths.pi = math.pi
    maths.e = math.e
    maths.tau = math.tau

############## bags ##############
bags = rli.PythonBasedLibrary('bags')
"""
"""

if True:

    @bags.modifier('flatten')
    def _(*, subject, context):
        # pylint: disable=redefined-outer-name
        bags = []
        current_bag = subject
        while current_bag.parent is not None:
            bags.append(current_bag)
            current_bag = current_bag.parent
        bags.append(current_bag)
        result = Bag(context)
        for bag in bags:
            result.load(bag)
        return result


############## rolls ##############
rolls = rli.PythonBasedLibrary('rolls')
"""
"""

############## strings ##############
strings = rli.PythonBasedLibrary('strings')
"""
"""
if True:

    @strings.modifier('lower')
    def _(*, subject, context):
        return subject.lower()

    @strings.modifier('upper')
    def _(*, subject, context):
        return subject.upper()

    @strings.modifier('strip')
    def _(*, subject, context):
        return subject.strip()

    @strings.modifier('split')
    def _(delim, times=None, *, subject, context):
        if times is None:
            return subject.split(delim)
        return subject.split(delim, times)


############## loading ##############
loading = rli.PythonBasedLibrary('loading')
"""
"""
if True:

    @loading.modifier('load_isolated')
    def _(*, subject, context):
        ...


BUILTIN_LIBRARIES = MappingProxyType({
    rootlib.name: rootlib,
    runtime.name: runtime,
    os.name: os,
    io.name: io,
    maths.name: maths,
    bags.name: bags,
    rolls.name: rolls,
    strings.name: strings,
    loading.name: loading,
})
