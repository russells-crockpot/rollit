"""
"""
import sys
from collections import ChainMap

from ..ast import elements
from ..exceptions import InvalidNameError, NoSuchLoopError, RollItSyntaxError
from .base import NoSubject

if sys.version_info.minor >= 8:
    from functools import cached_property
else:
    cached_property = property

__all__ = []


class Scope:
    """
    """
    __slots__ = ('_parent', '_isolated', '_loops', '_variables', '_subject', '_error', '_loop')

    # pylint: disable=protected-access, missing-param-doc
    def __init__(self, parent=None, *, isolate=False, subject=NoSubject, loop=None, error=None):
        """
        :param parent: The parent scope.
        :param bool isolate: When a scope is isolated, any values assigned will not override the
            values of the parent scope.
        """
        self._parent = parent
        self._isolated = isolate
        self._error = error
        self._loop = loop
        if not self._parent:
            self._loops = ChainMap()
            self._variables = ChainMap()
            self.subject = subject
        else:
            self._loops = ChainMap({}, *self._parent._loops.maps)
            self._variables = ChainMap({}, *self._parent._variables.maps)
            self.subject = subject if subject is not NoSubject else self._parent.subject
            self._error = error if error is not None else self._parent.error
            self._loop = loop if loop is not None else self._parent._loop

    def add_loop(self, name, loop):
        """
        """
        self._loops[name] = loop

    def get_loop(self, name):
        """
        """
        if name == elements.SpecialReference.NONE:
            return self.current_loop
        if name == elements.SpecialReference.ROOT:
            return self.root_loop
        try:
            return self._loops[name]
        except KeyError:
            raise NoSuchLoopError(name) from None

    def __contains__(self, key):
        return key in self._variables

    def __getitem__(self, name):
        if name == elements.SpecialReference.SUBJECT:
            if not self.in_modifier:
                raise RollItSyntaxError('Cannot refer to the subject outside of a modifier!')
            return self.subject
        if name == elements.SpecialReference.ROOT:
            return self.root
        if name == elements.SpecialReference.ERROR:
            return self.error
        if name == elements.SpecialReference.NONE:
            return None
        try:
            return self._variables[name]
        except KeyError:
            raise InvalidNameError(name) from None

    def __setitem__(self, name, value):
        if self._parent and not self._isolated and name in self._parent:
            self._parent[name] = value
        self._variables[name] = value

    #TODO protect parent scope?
    def __delitem__(self, name):
        if self._parent and not self._isolated and name in self._parent:
            del self._parent[name]
        del self._variables[name]

    def variable_names(self):
        """
        """
        return tuple(self._variables.keys())

    def loop_names(self):
        """
        """
        return tuple(self._loops.keys())

    @cached_property
    def error(self):
        """
        """
        if self._error or not self._parent:
            return self._error
        return self._parent.error

    @property
    def subject(self):
        """
        """
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
        self._variables['?'] = self._subject

    @cached_property
    def root_loop(self):
        """
        """
        if self._parent and self._parent.root_loop:
            return self._parent.root_loop
        return self._loop

    @cached_property
    def current_loop(self):
        """
        """
        if self._loop or not self._parent:
            return self._loop
        return self._parent.current_loop

    @cached_property
    def in_modifier(self):
        """
        """
        return self._subject is not NoSubject

    @cached_property
    def root(self):
        """
        """
        if self._parent:
            return self._parent.root
        return self
