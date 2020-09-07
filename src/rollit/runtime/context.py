"""
"""
from contextlib import contextmanager, suppress

from ..ast import elements, ModelElement, ModelEnumElement
from ..exceptions import RollitTypeError, CannotReduceError, InvalidNameError, RollitRuntimeError, \
        RollitReferenceError
from .base import is_atom
from .objects import Bag
from .scope import Scope

__all__ = ['RuntimeContext']


class RuntimeContext:
    """
    """
    _runner = None
    _accessing = None
    _root_scope = None
    _scope = None
    _allow_scope_access = True
    _libraries = None

    def __init__(self, runner):
        self._runner = runner
        self._accessing = self._root_scope = self._scope = Scope(context=self)
        self._libraries = {'~': self._runner.load_library('~', self)}
        self.root_scope.load(self._libraries['~'])

    def get_library(self, name):
        """
        """
        if name not in self._libraries:
            self._libraries[name] = self._runner.load_library(name, self)
        return self._libraries[name]

    @property
    def root_scope(self):
        """
        """
        return self._root_scope

    @property
    def accessing(self):
        """
        """
        return self._accessing

    @accessing.setter
    def accessing(self, value):
        if value is None:
            raise ValueError()
        self._accessing = value

    @property
    def subject(self):
        """
        """
        return self._scope.subject

    @property
    def scope(self):
        """
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

    def __getitem__(self, key):
        if isinstance(key, (elements.SpecialEntry, elements.RawAccessor)) \
                and not isinstance(self.accessing, Bag):
            raise RollitTypeError()
        try:
            return self.accessing[key]
        except (RollitReferenceError, InvalidNameError):
            if self.accessing != self._scope and self._allow_scope_access:
                with suppress(InvalidNameError, RollitReferenceError):
                    return self._scope[key]
            raise

    def __setitem__(self, name, value):
        self.accessing[name] = value

    def __delitem__(self, name):
        del self.accessing[name]

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return

    def roll(self, sides):
        """
        """
        return self._runner.dice_tower.roll(sides)

    def __call__(self, obj):
        return self.evaluate(obj)

    def evaluate(self, obj):
        """
        """
        if not isinstance(obj, ModelElement):
            return obj
        try:
            return obj.evaluate(self)
        except RollitRuntimeError as e:
            if not e.codeinfo and not isinstance(obj, ModelEnumElement):
                e.codeinfo = obj.codeinfo
            raise

    def reduce(self, obj):
        """
        """
        if is_atom(obj):
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
        while not is_atom(seen[-1]):
            reduced_value = self.reduce(seen[-1])
            if reduced_value in seen:
                raise RuntimeError()
            seen.append(reduced_value)
        return seen[-1]

    @contextmanager
    def now_access(self, accessing, *, allow_scope_access=True):
        """
        """
        if self.accessing != accessing or self._allow_scope_access != allow_scope_access:
            old_scope_access = self._allow_scope_access
            self._allow_scope_access = allow_scope_access
            old_accessing = self.accessing
            self.accessing = accessing
            yield self.accessing
            if old_accessing is None:
                self._accessing = None
            else:
                self.accessing = old_accessing
            self._allow_scope_access = old_scope_access
        else:
            yield

    @contextmanager
    def new_scope(self, parent_scope=None, **kwargs):
        """
        """
        if not parent_scope:
            parent_scope = self.scope
        old_accessing = self.accessing
        old_scope = self._scope
        self._scope = self.accessing = parent_scope.child(**kwargs)
        yield self._scope
        self.accessing = old_accessing
        self._scope = old_scope

    @contextmanager
    def use_subject(self, subject):
        """
        """
        old_subject = self.scope.subject
        self.scope.subject = subject
        yield
        self.scope.subject = old_subject
