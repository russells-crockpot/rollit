"""Contains the runtime context for rollit, which is what actually execute a parsed model.
"""
import contextvars
from abc import ABCMeta
from contextlib import contextmanager, suppress

from ..objects import Bag, NoSubject
from ..ast import elements, ModelElement
from ..exceptions import RollitTypeError, InvalidNameError, RollitRuntimeError, \
        RollitReferenceError, RollitSyntaxError
from .base import _CURRENT_CONTEXT, context as current_context

__all__ = ['RuntimeContext', 'Scope']


class RuntimeContext(metaclass=ABCMeta):
    """The runtime context is what actually evaluates and executes the parsed code. This includes
    keeping track of the scopes, loaded libraries, etcetera.

    A :class:`~.RuntimeContext` itself is callable. This is simply shorthand for the
    :meth:`~.evaluate` method.

    Similarly, values can be accessed/looked up by subscripting the context.
    """
    _runner = None
    _accessing = None
    _root_scope = None
    _scope = None
    _libraries = None
    _pycontext = None
    _reset_token = None

    def __init__(self, runner):
        reset_token = _CURRENT_CONTEXT.set(self)
        self._pycontext = contextvars.copy_context()
        _CURRENT_CONTEXT.reset(reset_token)
        self._runner = runner
        self._accessing = self._root_scope = self._scope = Scope()
        self._libraries = {'~': self._runner.load_library('~')}
        self.root_scope.load(self._libraries['~'])
        self.stack = []

    def get_library(self, name):
        """
        """
        if name not in self._libraries:
            self._libraries[name] = self._runner.load_library(name)
        return self._libraries[name]

    @property
    def root_scope(self):
        """The root scope.
        """
        return self._root_scope

    @property
    def accessing(self):
        """A context itself is always "accessing" something (except for a brief time upon its
        creation). Usually what it's accessing is current scope, however this is not always the
        case. Inside the execution for a bag definition, for example, the object currently being
        accessed is the new bag. Another example, when using the access expression ``a.b.c`` then
        the context first accesses ``a``, followed by ``b`` finally followed by ``c``. Unless
        specified otherwise, the current scope will always be accessible.

        To actually *change* what is being accessed, use the :meth:`~.now_access` context manager.
        """
        return self._accessing

    @property
    def subject(self):
        """
        """
        return self._scope.subject

    @property
    def scope(self):
        """The current scope.
        """
        return self._scope

    @scope.setter
    def scope(self, value):
        if value is None:
            raise ValueError()
        if value == elements.SpecialReference.ROOT:
            self._scope = self._root_scope
        self._scope = value

    def __contains__(self, name):
        if name in self.accessing:
            return True
        return name in self._scope

    # maybe allow "search_libraries"?
    def get_value(self, name, *, search_scope=True):
        """
        """
        if isinstance(name, (elements.SpecialEntry, elements.RawAccessor)) \
                and not isinstance(self.accessing, Bag):
            raise RollitTypeError()
        try:
            return self.accessing[name]
        except (RollitReferenceError, InvalidNameError):
            if self.accessing != self._scope and search_scope:
                with suppress(InvalidNameError, RollitReferenceError):
                    return self._scope[name]
            raise

    def __getitem__(self, key):
        return self.get_value(key)

    def __setitem__(self, name, value):
        self.accessing[name] = value

    def __delitem__(self, name):
        del self.accessing[name]

    def __enter__(self):
        if _CURRENT_CONTEXT.get() != self:
            self._reset_token = _CURRENT_CONTEXT.set(self)
        return self

    def __exit__(self, *args):
        if self._reset_token:
            _CURRENT_CONTEXT.reset(self._reset_token)
            self._reset_token = None

    def roll(self, sides):
        """
        """
        return self._runner.dice_tower.roll(sides)

    @contextmanager
    def _pushstack(self, obj):
        self.stack.append(obj)
        yield
        self.stack.pop()

    def __call__(self, obj):
        """
        """
        if not isinstance(obj, ModelElement):
            return obj
        try:
            with self._pushstack(obj):
                return obj.evaluate()
        except RollitRuntimeError as e:
            if not e.stacktrace:
                e.stacktrace = tuple(self.stack)
            raise

    @contextmanager
    def now_access(self, accessing):
        """
        """
        if self.accessing != accessing:
            old_accessing = self.accessing
            self._accessing = accessing
            yield self.accessing
            self._accessing = old_accessing
        else:
            yield

    @contextmanager
    def new_scope(self, parent_scope=None, **kwargs):
        """
        """
        if not parent_scope:
            parent_scope = self.scope
        old_scope = self._scope
        self._scope = parent_scope.child(**kwargs)
        with self.now_access(self._scope):
            yield self._scope
        self._scope = old_scope

    @contextmanager
    def use_subject(self, subject):
        """
        """
        old_subject = self.scope.subject
        self.scope.subject = subject
        yield
        self.scope.subject = old_subject


class Scope:
    """
    """
    __slots__ = ('parent', '_isolated', '_loops', '_variables', '_subject', '_error', '_loop')

    # pylint: disable=protected-access, missing-param-doc, missing-raises-doc
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
            self._variables = Bag()
            self._loops = []
            self.error = error
            self.subject = subject
        else:
            self._variables = Bag()
            self._loops = self.parent._loops[:]
            self.subject = subject if subject is not NoSubject else self.parent.subject
            self.error = error if error is not None else self.parent.error
            self._loop = loop if loop is not None else self.parent._loop

    def add_loop(self, name):
        """
        """
        self._loops.append(name)

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
            #pylint: disable=no-member
            return current_context.root_scope._variables
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
        return tuple(self._variables._entries.keys())

    @property
    def loops(self):
        """
        """
        return self._loops

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
