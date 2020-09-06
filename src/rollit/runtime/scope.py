"""
"""
from collections import ChainMap

from ..ast import elements
from ..exceptions import NoSuchLoopError, RollitSyntaxError, RollitReferenceError
from .objects import Bag
from .base import NoSubject

__all__ = []


class Scope:
    """
    """
    __slots__ = ('parent', '_isolated', '_loops', '_variables', '_subject', '_error', '_loop',
                 '_context')

    # pylint: disable=protected-access, missing-param-doc, missing-raises-doc
    def __init__(self,
                 parent=None,
                 *,
                 isolate=False,
                 subject=NoSubject,
                 loop=None,
                 error=None,
                 context=None):
        """
        :param parent: The parent scope.
        :param bool isolate: When a scope is isolated, any values assigned will not override the
            values of the parent scope.
        """
        self.parent = parent
        self._isolated = isolate
        self._loop = loop
        self._context = self._error = None
        self._subject = NoSubject
        if not self.parent:
            if not context:
                raise ValueError('A scope with no parent MUST have a context')
            self._context = context
            self._variables = Bag(self.context)
            self._loops = ChainMap()
            self.error = error
            self.subject = subject
        else:
            self._variables = Bag(self.context)
            self._loops = self.parent._loops.new_child()
            self.subject = subject if subject is not NoSubject else self.parent.subject
            self.error = error if error is not None else self.parent.error
            self._loop = loop if loop is not None else self.parent._loop

    @property
    def context(self):
        """
        """
        if self._context:
            return self._context
        return self.root._context

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
        return key in self._variables or (self.parent and key in self.parent)

    # pylint: disable=too-many-return-statements
    def __getitem__(self, name):
        if name in (elements.SpecialReference.SUBJECT, '?'):
            if not self.in_modifier:
                raise RollitSyntaxError('Cannot refer to the subject outside of a modifier!')
            return self.subject
        if name in (elements.SpecialReference.ROOT, '~'):
            return self.context.root_scope._variables
        if name in (elements.SpecialReference.LOCAL, '$'):
            return self._variables
        if name in (elements.SpecialReference.ERROR, '#'):
            return self.error
        if name in (elements.SpecialReference.NONE, '!'):
            return None
        if name in self._variables:
            return self._variables[name]
        if self.parent:
            return self.parent[name]
        raise RollitReferenceError(name)

    def __setitem__(self, name, value):
        if name in (elements.SpecialReference.SUBJECT, '?'):
            if self.subject is NoSubject:
                raise RollitSyntaxError()
            self.subject = value
            return
        if self.parent and not self._isolated and name in self.parent:
            self.parent[name] = value
        else:
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
        self._error = value

    @property
    def subject(self):
        """
        """
        return self._subject

    @subject.setter
    def subject(self, value):
        #FIXME This check will fail if the subject is the same in each modifier. For example, if the
        # subject is something like 2
        apply_to_parent = (self.parent and self.parent.subject is not NoSubject
                           and self.parent.subject is self._subject)
        self._subject = value
        if apply_to_parent:
            self.parent.subject = value

    def raw_get(self, name):
        """
        """
        if name in self._variables:
            return self._variables.raw_get(name)
        if self.parent:
            return self.parent.raw_get(name)
        raise RollitReferenceError(name)

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
