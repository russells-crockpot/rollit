# pylint: disable=protected-access, too-complex, using-constant-test,
# pylint: disable=no-method-argument, no-self-argument,missing-docstring
"""Contains the python code for the standard library.
"""
import math
import os
import sys
from contextlib import suppress
from types import MappingProxyType

from .base import context
from ..rli import cbool, blueprint as bp, subject_is_type
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


############## rootlib ##############
class RootLib(bp.LibraryBlueprints, name='~'):

    @bp.modifier
    def print(*args, subject):
        print(subject, *args)

    @bp.modifier
    def top(*args, subject):
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
    def bottom(*args, subject):
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

    @bp.modifier
    def input(*, subject):
        return input(subject)  # nosec


############## runtime ##############
class RuntimeLib(bp.LibraryBlueprints, name='runtime'):

    @bp.modifier
    def loops(*, subject):
        return Roll(context.scope.loops)

    @bp.modifier
    def scope_entries(*, subject):
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
    def names_in_scope(*, subject):
        names = set()
        scope = context.scope
        while scope.parent:
            names |= set(scope.variable_names())
            scope = scope.parent
        names |= set(scope.variable_names())
        names = Roll(sorted(names))
        return names

    @bp.modifier
    def overloads(*, subject):
        default = type(subject).default_ops_impl
        if default is None:
            default = OperatorImplementations()
        current = subject._op_impls
        bag = Bag()
        bag.setraw('left', Bag())
        bag.setraw('right', Bag())
        bag.setraw('other', Bag())
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
    def id(*args, subject):
        return subject.getid()

    @bp.modifier
    def overloaded_ops(*args, subject):
        default = type(subject).default_ops_impl
        if default is None:
            default = OperatorImplementations()
        current = subject._op_impls
        bag = Bag()
        bag.setraw('left', Bag())
        bag.setraw('right', Bag())
        bag.setraw('other', Bag())
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

    def on_access(name, *, subject):
        if name == 'cwd':
            return os.getcwd()
        if name == 'paths':
            return context.library_search_paths
        return subject.raw_get(name)


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

    def on_access(name, *, subject):
        if name == 'name':
            if sys.platform.startswith('linux'):
                return 'linux'
            if sys.platform.startswith('win'):
                return 'windows'
            if sys.platform.startswith('cygwin'):
                return 'cygwin'
            if sys.platform.startswith('darwin'):
                return 'macos'
            return sys.platform.rstrip('0123456789. -_')
        return subject.raw_get(name)

    envvars = bp.entry(_envvars)


############## io ##############
class IoFile(bp.BagBlueprints):
    """
    """

    @bp.modifier
    def create(filename, subject):
        """
        """
        bag = Bag()
        bag['name'] = filename
        bag[elements.SpecialEntry.PARENT] = subject
        return bag

    @bp.modifier
    def exists(*, subject):
        """
        """
        return os.path.exists(subject['name'])


class IoLib(bp.LibraryBlueprints, name='io'):
    """
    """
    File = bp.entry(IoFile())


############## maths ##############
class MathsLib(bp.LibraryBlueprints, name='maths'):
    """Yes, it's called ``maths`` and not ``math``. No I'm not British, but I like the way maths
    sounds better (also, everyone uses ``math``; it's boring).
    """
    pi = bp.entry(math.pi)
    e = bp.entry(math.e)
    tau = bp.entry(math.tau)


############## bags ##############
_subject_is_bag = subject_is_type(Bag)


class BagsLib(bp.LibraryBlueprints, name='bags'):
    """
    """

    @bp.modifier
    @_subject_is_bag
    def names(*, subject):
        return Roll(subject._entries.keys())

    @bp.modifier
    @_subject_is_bag
    def values(*, subject):
        return Roll(subject._entries.values())

    @bp.modifier
    @_subject_is_bag
    def flatten(*, subject):
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
_subject_is_roll = subject_is_type(Roll)


class RollsLib(bp.LibraryBlueprints, name='rolls'):
    """
    """

    @bp.modifier
    @_subject_is_roll
    def slice(start, end=-1, *, subject):
        return Roll(subject._items[start - 1:end])

    @bp.modifier
    @_subject_is_roll
    def insert(idx, item, *, subject):
        subject.insert(item, idx)

    @bp.modifier
    @_subject_is_roll
    def remove(start, end=None, *, subject):
        start -= 1
        if end is None:
            end = start
        del subject._items[start:end]

    @bp.modifier
    @_subject_is_roll
    #TODO allow for key
    def sort(*, subject):
        subject.sort()

    @bp.modifier
    @_subject_is_roll
    def count(item, *, subject):
        return subject._items.count(item)


############## strings ##############
class StringsLib(bp.LibraryBlueprints, name='strings'):
    """
    """

    @bp.modifier
    def lower(*, subject):
        """
        """
        return subject.lower()

    @bp.modifier
    def upper(*, subject):
        """
        """
        return subject.upper()

    @bp.modifier
    def strip(*, subject):
        """
        """
        return subject.strip()

    @bp.modifier
    def split(delim, times=None, *, subject):
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
    def load_isolated(*, subject):
        """
        """
        raise NotImplementedError()

    # pylint: disable=missing-function-docstring
    def on_access(name, *, subject):
        if name == 'paths':
            return context.library_search_paths
        return subject.raw_get(name)


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
