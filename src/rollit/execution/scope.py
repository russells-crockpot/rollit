"""
"""
from collections import ChainMap

from ..ast import elements
from ..exceptions import InvalidNameError, NoSuchLoopError, RollitSyntaxError
from ..internal_objects import Bag
from .base import NoSubject

__all__ = []


class Scope:
    """
    """
    __slots__ = ('parent', '_isolated', '_loops', '_variables', '_subject', '_error', '_loop')

    # pylint: disable=protected-access, missing-param-doc
    def __init__(self, parent=None, *, isolate=False, subject=NoSubject, loop=None, error=None):
        """
        :param parent: The parent scope.
        :param bool isolate: When a scope is isolated, any values assigned will not override the
            values of the parent scope.
        """
        self.parent = parent
        self._isolated = isolate
        self._loop = loop
        self._error = None
        self._subject = NoSubject
        if not self.parent:
            self._loops = ChainMap(Bag())
            self._variables = ChainMap(Bag())
            self.error = error
            self.subject = subject
        else:
            self._loops = ChainMap(Bag(), *self.parent._loops.maps)
            self._variables = ChainMap(Bag(), *self.parent._variables.maps)
            self.subject = subject if subject is not NoSubject else self.parent.subject
            self.error = error if error is not None else self.parent.error
            self._loop = loop if loop is not None else self.parent._loop

    def add_loop(self, name, loop):
        """
        """
        self._loops[name] = loop

    def get_loop(self, name):
        """
        """
        if name in (elements.SpecialReference.NONE, '!', None, ''):
            return self.current_loop
        if name in (elements.SpecialReference.ROOT, '~'):
            return self.root_loop
        try:
            return self._loops[name]
        except KeyError:
            raise NoSuchLoopError(name) from None

    def load(self, bag):
        """
        """
        # pylint: disable=protected-access
        if isinstance(bag, Scope):
            bag = bag._variables
        self._variables.update(bag)

    def __contains__(self, key):
        return key in self._variables

    def __getitem__(self, name):
        if name in (elements.SpecialReference.SUBJECT, '?'):
            if not self.in_modifier:
                raise RollitSyntaxError('Cannot refer to the subject outside of a modifier!')
            return self.subject
        if name in (elements.SpecialReference.ROOT, '~'):
            return self._variables.maps[-1]
        if name in (elements.SpecialReference.LOCAL, '$'):
            return Bag(self._variables)
        if name in (elements.SpecialReference.ERROR, '#'):
            return self.error
        if name in (elements.SpecialReference.NONE, '!'):
            return None
        try:
            return self._variables[name]
        except KeyError:
            raise InvalidNameError(name) from None

    def __setitem__(self, name, value):
        if name == '?':
            self.subject = value
            if self.parent and self.parent.subject is not NoSubject:
                self.parent['?'] = value
                return
        if self.parent and not self._isolated and name in self.parent:
            self.parent[name] = value
        self._variables[name] = value

    #TODO protect parent scope?
    def __delitem__(self, name):
        if self.parent and not self._isolated and name in self.parent:
            del self.parent[name]
        del self._variables[name]

    def variable_names(self):
        """
        """
        return tuple(self._variables.keys())

    def loop_names(self):
        """
        """
        return tuple(self._loops.keys())

    @property
    def error(self):
        """
        """
        if self._error or not self.parent:
            return self._error
        return self.parent.error

    @error.setter
    def error(self, value):
        if not value:
            self._variables.pop('#', None)
        else:
            self._variables['#'] = value
        self._error = value

    @property
    def subject(self):
        """
        """
        return self._subject

    @subject.setter
    def subject(self, value):
        if value is NoSubject:
            self._variables.pop('?', None)
        else:
            self._variables['?'] = value
        self._subject = value

    @property
    def root_loop(self):
        """
        """
        if self.parent and self.parent.root_loop:
            return self.parent.root_loop
        return self._loop

    @property
    def current_loop(self):
        """
        """
        if self._loop or not self.parent:
            return self._loop
        return self.parent.current_loop

    @property
    def in_modifier(self):
        """
        """
        return self._subject is not NoSubject

    @property
    def root(self):
        """
        """
        if self.parent:
            return self.parent.root
        return self

    def destroy(self):
        """
        """
        for k in tuple(self._variables.maps[0].keys()):
            del self._variables[k]
        for k in tuple(self._loops.maps[0].keys()):
            del self._loops[k]
        for a in self.__slots__:
            delattr(self, a)

    def child(self, **kwargs):
        """
        """
        return type(self)(self, **kwargs)
