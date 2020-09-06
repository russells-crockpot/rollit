"""
"""
import inspect

from .. import grammar
from ..ast import actions, ModelElement
from ..ast.util import flatten_tuple
from .base import DEFAULT_SEARCH_PATH
from .context import RuntimeContext
from .towers import DefaultTower

__all__ = ['Runner']


class Runner:
    """
    """

    def __init__(self,
                 search_path=DEFAULT_SEARCH_PATH,
                 *,
                 dice_tower=DefaultTower,
                 parser_options=None):
        if inspect.isclass(dice_tower):
            dice_tower = dice_tower()
        self.dice_tower = dice_tower
        self._context = RuntimeContext(runner=self)
        self._search_path = search_path
        self._libraries = {}

    def run(self, script):
        """
        """
        script_model = grammar.parse(script, actions=actions)
        if not isinstance(script_model, ModelElement) \
                and isinstance(script_model, (tuple, list)) and len(script_model) == 1:
            script_model = script_model[0]
        if not isinstance(script_model, ModelElement) \
                and isinstance(script_model, (tuple, list)):
            return tuple(self._context(item) for item in flatten_tuple(script_model))
        return self._context(script_model)

    def current_variable_names(self):
        """
        """
        # pylint: disable=protected-access
        self._context._scope.variable_names()

    def current_loop_names(self):
        """
        """
        # pylint: disable=protected-access
        self._context._scope.loop_names()
