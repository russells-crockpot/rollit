"""
"""
from collections import ChainMap

from ..ast import elements
from ..exceptions import NoSuchLoopError, RollitSyntaxError
from .objects import Bag
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
            self._variables = Bag(isolate=isolate)
            self._loops = ChainMap()
            self.error = error
            self.subject = subject
        else:
            self._variables = Bag(parent=parent._variables, isolate=isolate)
            self._loops = self.parent._loops.new_child()
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
        if name in (elements.SpecialAccessor.PARENT, '^'):
            parent = self.parent
            while parent and parent.current_loop == self.current_loop:
                parent = parent.parent
            if not parent or not parent.current_loop:
                raise NoSuchLoopError('^') from None
            return parent.current_loop
        if name in (elements.SpecialReference.ROOT, '~'):
            return self.root_loop
        try:
            return self._loops[name]
        except KeyError:
            raise NoSuchLoopError(name)

    def load(self, bag):
        """
        """
        # pylint: disable=protected-access
        if isinstance(bag, Scope):
            bag = bag._variables
        self._variables.load(bag)

    def __contains__(self, key):
        return key in self._variables

    def __getitem__(self, name):
        if name in (elements.SpecialReference.SUBJECT, '?'):
            if not self.in_modifier:
                raise RollitSyntaxError('Cannot refer to the subject outside of a modifier!')
            return self.subject
        if name in (elements.SpecialReference.ROOT, '~'):
            return self._variables.root
        if name in (elements.SpecialReference.LOCAL, '$'):
            return self._variables
        if name in (elements.SpecialReference.ERROR, '#'):
            return self.error
        if name in (elements.SpecialReference.NONE, '!'):
            return None
        return self._variables[name]

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
            del self._variables[elements.SpecialReference.ERROR]
        else:
            self._variables[elements.SpecialReference.ERROR] = value
        self._error = value

    @property
    def subject(self):
        """
        """
        return self._subject

    @subject.setter
    def subject(self, value):
        if value is NoSubject:
            del self._variables[elements.SpecialReference.SUBJECT]
        else:
            self._variables[elements.SpecialReference.SUBJECT] = value
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

    def child(self, **kwargs):
        """
        """
        return type(self)(self, **kwargs)
