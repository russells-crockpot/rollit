"""Items related to the Rollit Library Interface. And API used to create libraries for rollit in
python.
"""
import inspect
from abc import ABCMeta, abstractmethod
from collections import namedtuple
from contextlib import suppress

from .ast import ModelElement
from .ast.elements import SpecialEntry
from .objects import Modifier, Roll, Dice, Bag, NoSubject
from .util import is_valid_iterable

__all__ = [
    'ObjectPlaceholder',
    'BagPlaceholder',
    'PythonBasedModifier',
    'PythonBasedLibrary',
    'preloader',
    'postloader',
    'entry',
]


class ObjectPlaceholder(metaclass=ABCMeta):
    """
    """
    __slots__ = ('_preloaders', '_postloaders')

    def __init__(self, *, preloaders=None, postloaders=None):
        self._preloaders = preloaders if preloaders is not None else []
        self._postloaders = postloaders if postloaders is not None else []

    #TODO handle modifiers
    def _run_load_op(self, context, op, obj):
        if not op:
            return
        if is_valid_iterable(op):
            for item in op:
                self._run_load_op(context, item, obj)
        elif isinstance(op, ModelElement):
            context(op)
        elif callable(op):
            op(obj, context)
        else:
            raise TypeError()

    def resolve(self, context):
        """
        """
        for op in self._preloaders:
            self._run_load_op(context, op, self)
        obj = self.get_object(context)
        for op in self._postloaders:
            self._run_load_op(context, op, obj)
        return obj

    @abstractmethod
    def get_object(self, context):
        """
        """

    def preloader(self, func):
        """
        """
        self._preloaders.append(func)
        return func

    def postloader(self, func):
        """
        """
        self._postloaders.append(func)
        return func


class BagPlaceholder(ObjectPlaceholder):
    """
    """
    __slots__ = ('_entries', '_raw')

    def __init__(self, entries=None, raw=False, *, preloaders=None, postloaders=None):
        super().__init__(preloaders=preloaders, postloaders=postloaders)
        if entries is None:
            entries = {}
        self._entries = entries
        self._raw = raw

    def get_object(self, context):
        bag = Bag(context)
        for k, v in self._entries.items():
            if self._raw is True:
                bag.raw_set(k, v)
            else:
                bag[k] = v
        if isinstance(self._raw, dict):
            for k, v in self._raw.items():
                bag.raw_set(k, v)
        return bag

    def on_access(self, modifier):
        """
        """
        if not isinstance(modifier, Modifier):
            modifier = PythonBasedModifier(modifier)
        self._entries[SpecialEntry.ACCESS] = modifier

    def on_set(self, modifier):
        """
        """
        if not isinstance(modifier, Modifier):
            modifier = PythonBasedModifier(modifier)
        self._entries[SpecialEntry.SET] = modifier

    def on_clear(self, modifier):
        """
        """
        if not isinstance(modifier, Modifier):
            modifier = PythonBasedModifier(modifier)
        self._entries[SpecialEntry.CLEAR] = modifier

    def on_create(self, modifier):
        """
        """
        if not isinstance(modifier, Modifier):
            modifier = PythonBasedModifier(modifier)
        self._entries[SpecialEntry.CREATE] = modifier

    def on_destroy(self, modifier):
        """
        """
        if not isinstance(modifier, Modifier):
            modifier = PythonBasedModifier(modifier)
        self._entries[SpecialEntry.DESTROY] = modifier


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

    def modify(self, *args, context):
        val = self.func(*args, subject=context.scope.subject, context=context)
        if val not in (None, NoSubject):
            context.scope.subject = val

    @property
    def display_string(self):
        return self._display_string

    @display_string.setter
    def display_string(self, value):
        self._display_string = value


class PythonBasedLibrary:
    """
    """
    _initialized = False
    name = None
    """ """
    isolate = False
    """If ``True``, then the library will be loaded in it's own context."""
    raw = True
    """ """

    def __init__(self, name, entries=None, *, raw=True, isolate=False):
        self.name = name
        self.isolate = isolate
        self.raw = raw
        self._preloaders = []
        self._postloaders = []
        self._entries = {}
        if entries is None:
            entries = {}
        for key, value in entries.items():
            self[key] = value
        self._initialized = True

    def __setattr__(self, name, value):
        if self._initialized:
            with suppress(TypeError):
                self[name] = value
        return super().__setattr__(name, value)

    def modifier(self, name_or_func):
        """
        """
        if callable(name_or_func):
            # pylint: disable=no-member
            name = name_or_func.__name__
        else:
            name = name_or_func

        def _decorator(func):
            self._entries[name] = entry(func)
            return func

        if callable(name_or_func):
            return _decorator(name_or_func)
        return _decorator

    def add_entry(self, name, value, *, is_property=False):
        """
        """
        self._entries[name] = entry(value, is_property=is_property)

    def entry(self, name, *, is_property=True):
        """
        """

        def _decorator(entry_):
            self._entries[name] = entry(entry_, is_property=is_property)
            return entry_

        return _decorator

    def preloader(self, func):
        """
        """
        self._preloaders.append(func)

    def postloader(self, func):
        """
        """
        self._postloaders.append(func)

    def __setitem__(self, key, value):
        self._entries[key] = entry(value)

    def _get_entry_value(self, entry_info):
        value = entry_info.value
        if entry_info.is_property:
            if isinstance(value, property):
                value = value.__get__(self, type(self))
            elif callable(value):
                sig = inspect.signature(value)
                # pylint: disable=compare-to-zero
                if len(sig.parameters) == 0:
                    value = value()
                elif len(sig.parameters) == 1:
                    value = value(self)
                else:
                    raise ValueError()
            if not isinstance(value, _VALID_ENTRY_TYPES):
                value = self._get_entry_value(entry(value))
        if isinstance(value, PythonBasedLibrary):
            value = value.to_placeholder()
        return value

    # pylint: disable=protected-access
    def to_placeholder(self):
        """
        """
        preloaders = []
        postloaders = []
        entries = {}
        for attr in dir(self):
            entry_item = getattr(self, attr)
            if isinstance(entry_item, preloader):
                self._preloaders.append(entry_item.value)
                continue
            if isinstance(entry_item, postloader):
                self._postloaders.append(entry_item.value)
                continue
            if not isinstance(entry_item, entry):
                continue
            entries[attr] = self._get_entry_value(entry_item)
        preloaders += self._preloaders
        postloaders += self._postloaders
        for name, entry_item in self._entries.items():
            if not isinstance(entry_item, entry):
                continue
            entries[name] = self._get_entry_value(entry_item)
        return BagPlaceholder(
            entries,
            raw=self.raw,
            preloaders=preloaders,
            postloaders=postloaders,
        )

    def on_access(self, modifier):
        """
        """
        self._entries[SpecialEntry.ACCESS] = entry(modifier)

    def on_set(self, modifier):
        """
        """
        self._entries[SpecialEntry.SET] = entry(modifier)

    def on_clear(self, modifier):
        """
        """
        self._entries[SpecialEntry.CLEAR] = entry(modifier)

    def on_destroy(self, modifier):
        """
        """
        self._entries[SpecialEntry.DESTROY] = entry(modifier)


_VALID_ENTRY_TYPES = (int, str, Bag, Roll, Dice, ModelElement, Modifier, ObjectPlaceholder,
                      type(None), PythonBasedLibrary)


class _Loader(namedtuple('_LoaderBase', ('func',))):
    """
    """

    def __new__(cls, func):
        if isinstance(func, _Loader):
            func = func.func
        elif isinstance(func, entry):
            func = func.value
        return super().__new__(cls, func)


preloader = type('preloader', (_Loader,), {})
""" """

postloader = type('postloader', (_Loader,), {})
""" """


class entry(namedtuple('_EntryBase', ('value', 'is_property'))):
    """
    """

    def __new__(cls, value, *, is_property=False, raw=False):
        if not is_property:
            is_property = isinstance(value, property)
        if isinstance(value, entry):
            if value.is_property == is_property:
                return value
            return super().__new__(cls, value.value, is_property=is_property)
        if isinstance(value, _Loader):
            value = value.value
        if is_valid_iterable(value) and not isinstance(value, Roll):
            value = Roll(value)
        elif isinstance(value, dict):
            value = BagPlaceholder(value, raw=raw)
        elif callable(value) and not isinstance(value, _VALID_ENTRY_TYPES):
            value = PythonBasedModifier(value)
        # pylint: disable=consider-merging-isinstance
        if not (isinstance(value, _VALID_ENTRY_TYPES) or isinstance(value, property)):
            raise TypeError()
        return super().__new__(cls, value, is_property=is_property)

    def __getattr__(self, name):
        return getattr(self.value, name)

    def __setattr__(self, name, value):
        return setattr(self.value, name, value)

    def __delattr__(self, name):
        return delattr(self.value, name)
