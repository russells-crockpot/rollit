"""
"""
import inspect

from .. import grammar
from ..ast import actions, elements, flatten_tuple, is_valid_iterable, \
        ModelElement, SingleValueElement
from ..exceptions import RollItTypeError, NoneError, CannotReduceError, RollitIndexError, \
        RollitReferenceError
from .base import DEFAULT_SEARCH_PATH
from .scope import Scope
from .towers import DefaultTower

__all__ = ['ExecutionEnvironment', 'ExecutionContext']


class ExecutionEnvironment:
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
        self._context = ExecutionContext(env=self)
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


class ExecutionContext:
    """
    """

    def __init__(self, env):
        self._env = env
        self._root_scope = self._scope = Scope()

    def new_scope(self, **kwargs):
        """
        """
        return Scope(self._scope, **kwargs)

    def __contains__(self, name):
        return name in self._scope

    def __getitem__(self, name):
        return self._scope[name]

    def __setitem__(self, name, value):
        self._scope[name] = value

    def __delitem__(self, name):
        del self._scope[name]

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return

    def roll(self, sides):
        """
        """
        return self._env.dice_tower.roll(sides)

    def __call__(self, obj):
        return self.evaluate(obj)

    def evaluate(self, obj):
        """
        """
        if isinstance(obj, (int, float)) or obj is None:
            return obj
        if isinstance(obj, (str, elements.SpecialReference)):
            return self[obj]
        if isinstance(obj, elements.StringLiteral):
            return obj.value
        return obj.evaluate(self)

    def reduce(self, obj):
        """
        """
        if isinstance(obj, (int, float, str)) or obj is None:
            return obj
        try:
            return obj.reduce(self)
        except TypeError:
            raise CannotReduceError(obj)

    def full_reduce(self, obj):
        """
        """
        seen = []
        seen.append(self.reduce(obj))
        while seen[-1] is not None and not isinstance(seen[-1], (str, int, float)):
            reduced_value = self.reduce(seen[-1])
            if reduced_value in seen:
                raise RuntimeError()
            seen.append(reduced_value)
        return seen[-1]

    def access_obj(self, name, accessors):
        """
        """
        obj = self[name]
        for item in accessors:
            try:
                if obj is None or item not in obj:
                    raise NoneError()
                obj = obj[item]
            except TypeError:
                raise RollItTypeError()
        return obj

    def evaluate_children(self, obj):
        """Evaluates all of the children of a :class:`~rollit.ast.ModelElement` and returns an
        object that is exactly the same, but each attribute has been evaluated.

        .. warning::

            If the element is a :class:`~rollit.ast.SingleValueElement`, then that element's
            evaluated value is returned instead of a copy of the element itself.
        """
        if isinstance(obj, (int, float)) or obj is None:
            return obj
        if is_valid_iterable(obj):
            return type(obj)(self.evaluate_children(o) for o in obj)
        if not isinstance(obj, ModelElement):
            return self.evaluate(obj)
        if isinstance(obj, SingleValueElement):
            return self.evaluate(obj.value)
        return type(obj)(**{
            k: self.evaluate(v) for k, v in obj._asdict().items() if k != 'codeinfo'
        },
                         codeinfo=obj.codeinfo)

    #pylint: disable = too-complex
    def _access(self, accessing, accessor):
        if accessing in (None, elements.SpecialReference.NONE):
            raise NoneError()
        try:
            if isinstance(accessor, elements.SpecialAccessor):
                if accessor == elements.SpecialAccessor.LENGTH:
                    return len(accessing)
                if accessor == elements.SpecialAccessor.VALUE:
                    return accessing.value
                if accessor == elements.SpecialAccessor.TOTAL:
                    return accessing.total
                raise NotImplementedError()
            if isinstance(accessor, (str, int)):
                return accessing[accessor]
            if isinstance(accessor, elements.Reduce):
                return self.access(accessing, self.reduce(accessor))
            return accessing[accessor]
        except TypeError:
            raise RollItTypeError()
        except (AttributeError, KeyError):
            raise RollitReferenceError()
        except IndexError:
            raise RollitIndexError()

    def access(self, accessing, *accessors):
        """
        """
        if not accessors:
            return accessing
        for accessor in accessors:
            accessing = self._access(accessing, accessor)
        return accessing
