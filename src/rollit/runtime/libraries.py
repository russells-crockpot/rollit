"""
"""
import os
import pathlib
import re
from collections import namedtuple

from ..exceptions import RollitTypeError, LibraryNotFoundError
from ..util import ensure_tuple
from .objects import PythonBasedModifier, ObjectPlaceholder, BagPlaceholder, Roll, Dice, Bag

__all__ = [
    'LibraryLoader',
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


root = BagPlaceholder({
    'print': _print,
    'top': _top,
    'bottom': _bottom,
})


@PythonBasedModifier
# pylint: disable=protected-access
def _loops(*args, subject, context):
    return Roll(context.scope.loops)


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


runtime = BagPlaceholder({
    'in_scope': _in_scope,
    'names_in_scope': _names_in_scope,
    'loops': _loops,
})


class LibraryLoader:
    """
    """
    __slots__ = ('libraries', '_paths', '_runner')
    _FILE_SUFFIX_PAT = re.compile(r'\.(py[coz]?|rollit)', re.I)
    LibraryInfo = namedtuple('LibraryInfo', ('name', 'file', 'type', 'content'))
    """ """

    def __init__(self, paths, runner):
        self._paths = None
        self.paths = paths
        self._runner = runner
        self.libraries = {
            '~': self.LibraryInfo('~', __file__, 'python', root),
            'runtime': self.LibraryInfo('runtime', __file__, 'python', runtime),
        }

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
            if isinstance(info.content, ObjectPlaceholder):
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
