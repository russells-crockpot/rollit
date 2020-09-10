# pylint: disable=protected-access, too-complex, using-constant-test
"""Contains the python code for the standard library.
"""
import math
import os
import sys
from contextlib import suppress
from types import MappingProxyType

from .base import context
from ..rli import cbool, blueprint as bp
from ..rli.deferred import BagPlaceholder
from ..ast import elements
from ..exceptions import RollitTypeError
from ..objects import Roll, Dice, Bag, OperatorImplementations

__all__ = [
    'RootLib',
    'RuntimeLib',
    'BagsLib',
    'OsLib',
    'IoLib',
    'MathsLib',
    'RollsLib',
    'StringsLib',
    'LoadingLib',
    'BUILTIN_LIBRARIES',
]
#########################################################
# Note: The contents of each library is in a ``if True``
# block because it makes folding code easier and the code
# in general look cleaner/more organized.
#########################################################

############## rootlib ##############


class RootLib(bp.LibraryBlueprints, name='~'):
    """
    """

    @bp.modifier
    # pylint: disable=useless-return
    def print(self, *args, subject):
        """
        """
        print(subject, *args)
        return None

    @bp.modifier
    def top(self, *args, subject):
        """
        """
        if not args:
            num = 1
        else:
            num = args[0]
        if isinstance(subject, Dice):
            # pylint: disable=too-many-function-args
            subject = context(elements.Reduce(subject, codeinfo=None))
        if not isinstance(subject, Roll):
            raise RollitTypeError()
        return Roll(sorted(subject, reverse=True)[0:num])

    @bp.modifier
    def bottom(self, *args, subject):
        """
        """
        if not args:
            num = 1
        else:
            num = args[0]
        if isinstance(subject, Dice):
            # pylint: disable=too-many-function-args
            subject = context(elements.Reduce(subject, codeinfo=None))
        if not isinstance(subject, Roll):
            raise RollitTypeError()
        return Roll(sorted(subject)[0:num])


############## runtime ##############


class RuntimeLib(bp.LibraryBlueprints, name='runtime'):
    """
    """

    @bp.modifier
    def loops(self, *, subject):
        """
        """
        return Roll(context.scope.loops)

    @bp.modifier
    def scope_entries(self, *, subject):
        """
        """
        scopes = []
        scope = context.scope
        while scope.parent:
            scopes.append(scope._variables._entries)
            scope = scope.parent
        scopes.append(scope._variables._entries)
        entries = {}
        for scope in reversed(scopes):
            entries.update(scope)
        bag = Bag()
        bag._entries = entries
        return bag

    @bp.modifier
    def names_in_scope(self, *, subject):
        """
        """
        names = set()
        scope = context.scope
        while scope.parent:
            names |= set(scope.variable_names())
            scope = scope.parent
        names |= set(scope.variable_names())
        names = Roll(names)
        names.sort()
        return names

    @bp.modifier
    def overloads(self, *, subject):
        """
        """
        default = type(subject).default_ops_impl
        if default is None:
            default = OperatorImplementations()
        current = subject._op_impls
        bag = Bag()
        bag.set_raw('left', Bag())
        bag.set_raw('right', Bag())
        bag.set_raw('other', Bag())
        for op in elements.TwoSidedOperator:
            rval = getattr(current, op.right_python_name)
            if rval is not NotImplemented:
                if rval is not getattr(default, op.right_python_name):
                    bag['right'].raw_set(op.name.lower(), rval)
            lval = getattr(current, op.left_python_name)
            if lval is not NotImplemented:
                if lval is not getattr(default, op.left_python_name):
                    bag['left'].raw_set(op.name.lower(), lval)
        for op in elements.OneSidedOperator:
            val = getattr(current, op.python_name)
            if val is not NotImplemented:
                if val is not getattr(default, op.left_python_name):
                    bag['other'].raw_set(op.name.lower(), val)
        for op in elements.OneSidedOperator:
            val = getattr(current, op.python_name)
            if val is not NotImplemented:
                if val is not getattr(default, op.left_python_name):
                    bag['other'].raw_set(op.name.lower(), val)
        return bag

    @bp.modifier
    def overloaded_ops(self, *args, subject):
        """
        """
        default = type(subject).default_ops_impl
        if default is None:
            default = OperatorImplementations()
        current = subject._op_impls
        bag = Bag()
        bag.set_raw('left', Bag())
        bag.set_raw('right', Bag())
        bag.set_raw('other', Bag())
        for op in elements.TwoSidedOperator:
            bag['left'].raw_set(
                op.name.lower(),
                cbool(
                    getattr(current, op.left_python_name) is not getattr(
                        default, op.left_python_name)))
            bag['right'].raw_set(
                op.name.lower(),
                cbool(
                    getattr(current, op.right_python_name) is not getattr(
                        default, op.right_python_name)))
        for op in elements.OneSidedOperator:
            bag['other'].raw_set(
                op.name.lower(),
                cbool(getattr(current, op.python_name) is not getattr(default, op.python_name)))
        for op in elements.OneSidedOperator:
            bag['other'][op.name.lower()] = cbool(
                getattr(current, op.python_name) is not getattr(default, op.python_name))
        return bag

    # pylint: disable=missing-function-docstring
    def on_access(self, name, lib):
        if name == 'cwd':
            return os.getcwd()
        return lib.raw_get(name)


############## os ##############
_envvars = BagPlaceholder()


@_envvars.on_access
def _(name, subject):
    with suppress(KeyError):
        return os.environ[context(name)]
    return None


@_envvars.on_set
def _(name, value, subject):
    os.environ[context(name)] = str(context(value))


class OsLib(bp.LibraryBlueprints, name='os'):
    """
    """

    @bp.entry
    def name_(self):
        """
        """
        if sys.platform.startswith('linux'):
            return 'linux'
        if sys.platform.startswith('win'):
            return 'windows'
        if sys.platform.startswith('cygwin'):
            return 'cygwin'
        if sys.platform.startswith('darwin'):
            return 'macos'
        return sys.platform.rstrip('0123456789. -_')

    envvars = bp.entry(_envvars)


############## io ##############
class IoFile(bp.BagBlueprints):
    """
    """

    @bp.modifier
    def create(self, filename, subject):
        """
        """
        bag = Bag()
        bag['name'] = filename
        bag[elements.SpecialEntry.PARENT] = subject
        return bag

    @bp.modifier
    def exists(self, *, subject):
        """
        """
        return os.path.exists(subject['name'])


class IoLib(bp.LibraryBlueprints, name='io'):
    """
    """
    File = bp.entry(IoFile)


############## maths ##############


class MathsLib(bp.LibraryBlueprints, name='maths'):
    """Yes, it's called ``maths`` and not ``math``. No I'm not British, but I like the way maths
    sounds better (also, everyone uses ``math``; it's boring).
    """
    pi = bp.entry(math.pi)
    e = bp.entry(math.e)
    tau = bp.entry(math.tau)


############## bags ##############
class BagsLib(bp.LibraryBlueprints, name='bags'):
    """
    """

    @bp.modifier
    def flatten(self, *, subject):
        """
        """
        # pylint: disable=redefined-outer-name
        bags = []
        current_bag = subject
        while current_bag.parent is not None:
            bags.append(current_bag)
            current_bag = current_bag.parent
        bags.append(current_bag)
        result = Bag()
        for bag in bags:
            result.load(bag)
        return result


############## rolls ##############
class RollsLib(bp.LibraryBlueprints, name='rolls'):
    """
    """


############## strings ##############
class StringsLib(bp.LibraryBlueprints, name='strings'):
    """
    """

    @bp.modifier
    def lower(self, *, subject):
        """
        """
        return subject.lower()

    @bp.modifier
    def upper(self, *, subject):
        """
        """
        return subject.upper()

    @bp.modifier
    def strip(self, *, subject):
        """
        """
        return subject.strip()

    @bp.modifier
    def split(self, delim, times=None, *, subject):
        """
        """
        if times is None:
            return subject.split(delim)
        return subject.split(delim, times)


############## loading ##############
class LoadingLib(bp.LibraryBlueprints, name='loading'):
    """
    """

    @bp.modifier
    def isolated(self, *, subject):
        """
        """
        raise NotImplementedError()


BUILTIN_LIBRARIES = MappingProxyType({
    RootLib.name: RootLib,
    RuntimeLib.name: RuntimeLib,
    OsLib.name: OsLib,
    IoLib.name: IoLib,
    MathsLib.name: MathsLib,
    BagsLib.name: BagsLib,
    RollsLib.name: RollsLib,
    StringsLib.name: StringsLib,
    LoadingLib.name: LoadingLib,
})
