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

    def run(self, script):
        """
        """
        script_model = self.parse(script)
        if not isinstance(script_model, ModelElement) \
                and isinstance(script_model, (tuple, list)) and len(script_model) == 1:
            script_model = script_model[0]
        if not isinstance(script_model, ModelElement) \
                and isinstance(script_model, (tuple, list)):
            return tuple(self._default_context(item) for item in flatten_tuple(script_model))
        return self._default_context(script_model)

    def load_library(self, name, context):
        """
        """

    @contextmanager
    def brief_context(self):
        """
        """
        yield RuntimeContext(runner=self)
