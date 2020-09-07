# pylint: disable=protected-access
"""
"""
import os
import pathlib
import re
from collections import namedtuple

from ..exceptions import RollitTypeError, LibraryNotFoundError
from ..util import ensure_tuple
from ..objects import Roll, Dice, Bag
from .. import lai

__all__ = [
    'LibraryLoader',
]

_rootlib = lai.PythonBasedLibrary('~')


@_rootlib.modifier('print')
# pylint: disable=useless-return
def _(*args, subject, context):
    print(subject, *args)
    return None


@_rootlib.modifier('top')
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


@_rootlib.modifier('bottom')
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


_runtime = lai.PythonBasedLibrary('runtime')


@_runtime.modifier('loops')
def _(*args, subject, context):
    return Roll(context.scope.loops)


@_runtime.modifier('scope_entries')
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


@_runtime.modifier('names_in_scope')
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


_BUILTIN_LIBS = (
    _rootlib,
    _runtime,
)


class LibraryLoader:
    """
    """
    __slots__ = ('libraries', '_paths', '_runner')
    _FILE_SUFFIX_PAT = re.compile(r'\.(py[coz]?|rollit)', re.I)
    LibraryInfo = namedtuple('LibraryInfo', ('name', 'file', 'type', 'content', 'isolate'))
    """ """

    def __init__(self, paths, runner):
        self._paths = None
        self.paths = paths
        self._runner = runner
        self.libraries = {}
        for lib in _BUILTIN_LIBS:
            self._add_from_lai_lib(lib, __file__)

    def _add_from_lai_lib(self, lib, path):
        info = self.LibraryInfo(lib.name, path, 'python', lib.to_placeholder(), lib.isolate)
        self.libraries[info.name] = info

    @property
    def paths(self):
        """
        """
        return self._paths

    @paths.setter
    def paths(self, value):
        self._paths = [pathlib.Path(p) for p in value]

    def get_library(self, library_name, context):
        """
        """
        self.load_library(library_name)
        info = self.libraries[library_name]
        if info.type == 'python':
            if isinstance(info.content, lai.ObjectPlaceholder):
                return info.content.resolve(context)
            raise TypeError(f'Expected and ObjectPlaceholder but got {type(info.content)}')
        if info.type == 'rollit':
            with self._runner.brief_context() as ctx:
                self._runner.run(info.content, context=ctx)
                # pylint: disable=protected-access
                return ctx.root_scope._variables
        raise ValueError(f'Unknown library type: {info.type}')

    def load_library(self, library_name, *, force_reload=False):
        """
        """
        if force_reload or library_name not in self.libraries:
            path = self.find_library(library_name)
            if not path:
                raise LibraryNotFoundError(library_name)
            if path.casefold().endswith('.rollit'):
                self.load_rollit_library(library_name, path, force_reload=force_reload)
            else:
                self.load_python_library(library_name, path, force_reload=force_reload)

    def load_python_library(self, name, file_path, *, force_reload=False):
        """
        """
        raise NotImplementedError()

    def load_rollit_library(self, name, file_path, *, force_reload=False):
        """
        """
        if not force_reload and name in self.libraries:
            return
        with open(file_path) as f:
            model = ensure_tuple(self._runner.parse(f.read()))
        self.libraries[name] = self.LibraryInfo(name, str(file_path), 'rollit', model)

    def find_library(self, name):
        """
        """
        if name in self.libraries:
            return self.libraries[name].file
        suffix = None
        if '.' in name:
            suffix, name = name.rspilt('.', 1)
            suffix = suffix.replace('.', os.sep)
        for base_path in self.paths:
            if suffix:
                base_path /= suffix
            for filename in base_path.iterdir():
                if filename.stem == name and self._FILE_SUFFIX_PAT.fullmatch(filename.suffix):
                    return str(filename)
        return None
