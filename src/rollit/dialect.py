"""
"""
from collections import ChainMap
from contextlib import suppress

from .model import Modifier
from .exceptions import InvalidNameError

__all__ = ['Dialect']


class Dialect:
    """
    """
    _ALL_DIALECTS = {}
    substitutions = None
    modifiers = None
    macros = None
    _is_root = None

    def __new__(cls, name=None, parent=None, **kwargs):
        if name and name in cls._ALL_DIALECTS:
            return cls._ALL_DIALECTS[name]
        return object.__new__(cls)

    def __init__(self, name=None, parent=None, *, is_root=False):
        if name and name in self._ALL_DIALECTS:
            return
        self.name = name
        if not parent:
            self.substitutions = ChainMap()
            self.modifiers = ChainMap()
            self.macros = ChainMap()
        else:
            self.substitutions = ChainMap({}, *parent.substitutions.maps)
            self.modifiers = ChainMap({}, *parent.modifiers.maps)
            self.macros = ChainMap({}, *parent.macros.maps)
        self.parent = parent
        self._is_root = is_root or not self.parent

    def child(self, name=None, *, is_root=False):
        """
        """
        return type(self)(name=name, parent=self, is_root=is_root)

    @classmethod
    def get_dialect(cls, name):
        """
        """
        if name not in cls._ALL_DIALECTS:
            raise InvalidNameError()
        return cls._ALL_DIALECTS[name]

    @classmethod
    def get_or_create_dialect(cls, name, parent):
        """
        """
        if isinstance(parent, str):
            parent = cls.get_dialect(parent)
        if name:
            with suppress(InvalidNameError):
                current_dialect = cls.get_dialect(name)
                if current_dialect.parent != parent:
                    #TODO
                    raise ValueError()
                return current_dialect
        return cls(name, parent)

    def add_alias(self, alias, name):
        """
        """
        if name in self.substitutions:
            self.substitutions[alias] = self.substitutions[name]
            self.modifiers.pop(alias, None)
        elif name in self.modifiers:
            self.modifiers[alias] = self.modifiers[name]
            self.substitutions.pop(alias, None)
        else:
            raise InvalidNameError()

    def add_substitution(self, name, value):
        """
        """
        self.substitutions[name] = value

    def get_substitution(self, name):
        """
        """
        if name not in self.substitutions:
            raise InvalidNameError()
        return self.substitutions[name]

    def add_modifier(self, name, definition):
        """
        """
        self.modifiers[name] = definition

    def get_macro(self, name):
        """
        """
        if name not in self.macros:
            raise InvalidNameError()
        return self.macros[name]

    def add_macro(self, macro):
        """
        """
        self.macros[macro.name] = macro

    def get_modifier(self, name):
        """
        """
        if name not in self.modifiers:
            raise InvalidNameError()
        return self.modifiers[name]

    @property
    def root(self):
        """
        """
        if self._is_root:
            return self
        return self.parent.root

    def modifier(self, func):
        """
        """
        self.add_modifier(func.__name__, Modifier(run=func, help=getattr(func, '__doc__', None)))
        return func
