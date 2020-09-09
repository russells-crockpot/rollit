"""
"""
import inspect
import os
import pathlib
import re
from collections import namedtuple

from .. import grammar, rli
from ..ast import actions, ModelElement
from ..ast.util import flatten_tuple
from ..exceptions import LibraryNotFoundError
from ..util import ensure_tuple
from . import libraries
from .base import DEFAULT_SEARCH_PATHS, context as current_ctx
from .core import RuntimeContext
from .towers import DefaultTower

__all__ = ['Runner', 'LibraryLoader']


class LibraryLoader:
    """Finds and loads libraries used by rollit.
    """
    __slots__ = ('libraries', '_paths', '_runner')
    _FILE_SUFFIX_PAT = re.compile(r'\.(py[coz]?|rollit)', re.I)
    LibraryInfo = namedtuple('LibraryInfo', ('name', 'file', 'type', 'content', 'isolate'))
    """Information about a library that has been loaded."""

    def __init__(self, paths, runner):
        self._paths = None
        self.paths = paths
        self._runner = runner
        self.libraries = {}
        self._add_from_lai_lib(libraries.rootlib, libraries.__file__)

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

    def get_library(self, library_name):
        """
        """
        self.load_library(library_name)
        info = self.libraries[library_name]
        if info.type == 'python':
            if isinstance(info.content, rli.ObjectPlaceholder):
                return info.content.resolve()
            raise TypeError(f'Expected and ObjectPlaceholder but got {type(info.content)}')
        if info.type == 'rollit':
            with self._runner.brief_context() as ctx:
                self._runner.run(info.content)
                # pylint: disable=protected-access
                return ctx.root_scope._variables
        raise ValueError(f'Unknown library type: {info.type}')

    def load_stdlib(self, library_name, *, force_reload=False):
        """
        """
        if force_reload or library_name not in self.libraries:
            if library_name not in libraries.BUILTIN_LIBRARIES:
                raise LibraryNotFoundError(library_name)
            self._add_from_lai_lib(libraries.BUILTIN_LIBRARIES[library_name], libraries.__file__)

    def load_library(self, library_name, *, force_reload=False):
        """Loads a library so that it will be accessible.

        .. note::

            This *only* loads the library, and makes it available; it still needs to be retrieved
            via the :meth:`~.get_library` method.
        """
        if library_name.startswith('~.'):
            self.load_stdlib(library_name[2:], force_reload=force_reload)
        elif force_reload or library_name not in self.libraries:
            path = self.find_library(library_name)
            if not path:
                if library_name in libraries.BUILTIN_LIBRARIES:
                    self.load_stdlib(library_name, force_reload=force_reload)
                else:
                    raise LibraryNotFoundError(library_name)
            elif path.casefold().endswith('.rollit'):
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


class Runner:
    """
    """

    def __init__(self,
                 search_paths=DEFAULT_SEARCH_PATHS,
                 *,
                 dice_tower=DefaultTower,
                 parser_options=None):
        if inspect.isclass(dice_tower):
            dice_tower = dice_tower()
        self.dice_tower = dice_tower
        self._library_loader = LibraryLoader(search_paths, self)
        self._default_context = RuntimeContext(runner=self)

    def parse(self, script):
        """
        """
        return grammar.parse(script, actions=actions)

    def run(self, script_or_model, context=None):
        """
        """
        if not context:
            context = self._default_context
        # pylint: disable=protected-access
        return context._pycontext.run(self._run, script_or_model)

    def _run(self, script_or_model):
        model = script_or_model
        if isinstance(script_or_model, (bytes, str)):
            model = self.parse(script_or_model)
        if not isinstance(model, ModelElement) \
                and isinstance(model, (tuple, list)) and len(model) == 1:
            model = model[0]
        if not isinstance(model, ModelElement) \
                and isinstance(model, (tuple, list)):
            return tuple(current_ctx(item) for item in flatten_tuple(model))
        return current_ctx(model)

    def load_library(self, name):
        """
        """
        return self._library_loader.get_library(name)

    def brief_context(self):
        """
        """
        yield RuntimeContext(runner=self)
