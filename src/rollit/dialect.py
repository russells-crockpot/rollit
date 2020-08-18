"""
"""
from collections import ChainMap

from .elements import Modifier
from .exceptions import InvalidNameError

__all__ = ['Dialect']


class Dialect:
    """
    """
    holder = None
    variables = None
    modifiers = None
    macros = None
    _is_root = None

    def __new__(cls, name=None, parent=None, **kwargs):
        if name and name in kwargs.get('holder', {}):
            return kwargs['holder'][name]
        return object.__new__(cls)

    def __init__(self, name=None, parent=None, *, is_root=False, holder=None):
        if name and holder and name in holder:
            return
        self.name = name
        if holder is None:
            if parent:
                holder = parent.holder
            else:
                holder = {}
        self.holder = holder
        if not parent:
            self.variables = ChainMap()
            self.modifiers = ChainMap()
            self.macros = ChainMap()
        else:
            self.variables = ChainMap({}, *parent.variables.maps)
            self.modifiers = ChainMap({}, *parent.modifiers.maps)
            self.macros = ChainMap({}, *parent.macros.maps)
        self.parent = parent
        self._is_root = is_root or not self.parent

    def child(self, name=None, *, is_root=False, holder=None):
        """
        """
        return type(self)(name=name, parent=self, is_root=is_root, holder=holder)

    def add_alias(self, alias, name):
        """
        """
        if name in self.variables:
            self.variables[alias] = self.variables[name]
            self.modifiers.pop(alias, None)
        elif name in self.modifiers:
            self.modifiers[alias] = self.modifiers[name]
            self.variables.pop(alias, None)
        else:
            raise InvalidNameError()

    def add_variable(self, name, value):
        """
        """
        self.variables[name] = value

    def get_variable(self, name):
        """
        """
        if name not in self.variables:
            raise InvalidNameError()
        return self.variables[name]

    def add_modifier(self, name, definition):
        """
        """
        self.modifiers[name] = definition

    def get_modifier(self, name):
        """
        """
        if name not in self.modifiers:
            raise InvalidNameError()
        return self.modifiers[name]

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
