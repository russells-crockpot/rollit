"""
"""
import inspect
from contextlib import contextmanager

from .. import grammar
from ..ast import actions, ModelElement
from ..ast.util import flatten_tuple
from .base import DEFAULT_SEARCH_PATHS
from .context import RuntimeContext
from .libraries import LibraryLoader
from .towers import DefaultTower

__all__ = ['Runner']


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

    def run(self, script_or_model, *, context=None):
        """
        """
        if context is None:
            context = self._default_context
        model = script_or_model
        if isinstance(script_or_model, (bytes, str)):
            model = self.parse(script_or_model)
        if not isinstance(model, ModelElement) \
                and isinstance(model, (tuple, list)) and len(model) == 1:
            model = model[0]
        if not isinstance(model, ModelElement) \
                and isinstance(model, (tuple, list)):
            return tuple(context(item) for item in flatten_tuple(model))
        return context(model)

    def load_library(self, name, context):
        """
        """
        return self._library_loader.get_library(name, context)

    @contextmanager
    def brief_context(self):
        """
        """
        yield RuntimeContext(runner=self)
