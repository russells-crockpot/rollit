"""Items related to the Rollit Library Interface; an API used to create libraries for rollit in
python.

.. seealso::

   :mod:`rollit.runtime.libraries` for examples.
"""
from abc import ABCMeta, abstractmethod

from ..ast.elements import SpecialEntry
from ..objects import Modifier, Bag, NoSubject
from ..runtime import context

__all__ = [
    'PythonBasedModifier',
    'PythonBasedLibrary',
    'PythonBag',
    'cbool',
]


class PythonBasedModifier(Modifier):
    """
    """
    __slots__ = (
        '_display_string',
        'func',
    )

    def __init__(self, func):
        self.func = func
        self._display_string = f'[-built-in modifier: {self.func.__name__.lstrip("_")}-]'

    def modify(self, *args):
        val = self.func(*args, subject=context.scope.subject)
        if val == NoSubject:
            context.scope.subject = None
        elif val is not None:
            context.scope.subject = val

    @property
    def display_string(self):
        return self._display_string

    @display_string.setter
    def display_string(self, value):
        self._display_string = value


def _to_mod(func):
    if not isinstance(func, PythonBasedModifier):
        return PythonBasedModifier(func)
    return func


def cbool(value):
    """
    """
    return 1 if value else 0


class PythonBag(Bag):
    """
    """

    def __init__(self, entries=None):
        super().__init__()
        if entries is not None:
            self.entries = entries

    def modifier(self, name_or_func):
        """
        """
        if callable(name_or_func):
            # pylint: disable=no-member
            name = name_or_func.__name__
        else:
            name = name_or_func

        def _decorator(func):
            self._entries[name] = _to_mod(func)
            return func

        if callable(name_or_func):
            return _decorator(name_or_func)
        return _decorator

    def on_create(self, modifier):
        """
        """
        self._entries[SpecialEntry.CREATE] = _to_mod(modifier)

    def on_access(self, modifier):
        """
        """
        self._entries[SpecialEntry.ACCESS] = _to_mod(modifier)

    def on_set(self, modifier):
        """
        """
        self._entries[SpecialEntry.SET] = _to_mod(modifier)

    def on_clear(self, modifier):
        """
        """
        self._entries[SpecialEntry.CLEAR] = _to_mod(modifier)

    def on_destroy(self, modifier):
        """
        """
        self._entries[SpecialEntry.DESTROY] = _to_mod(modifier)


class PythonBasedLibrary(metaclass=ABCMeta):
    """
    """

    @property
    @abstractmethod
    def name(self):
        """
        """

    @property
    @abstractmethod
    def isolate(self):
        """
        """
