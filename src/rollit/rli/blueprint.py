"""
"""
from ..ast import elements
from .base import PythonBasedLibrary
from .deferred import DeferredPythonBasedLibrary, DeferredBag

__all__ = [
    'modifier',
    'entry',
    'preloader',
    'postloader',
    'overload_op',
    'BagBlueprints',
    'LibraryBlueprintsMeta',
    'LibraryBlueprints',
]

_SPECIAL_OP_METHOD_NAMES = frozenset((
    'on_access',
    'on_create',
    'on_clear',
    'on_destroy',
    'on_set',
))


class _EntryDescriptor:
    __slots__ = ('value',)

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner=None):
        if instance:
            return self.value
        return self


class _FunctionEntryDescriptor(_EntryDescriptor):
    __slots__ = ('__isabstractmethod__',)

    def __get__(self, instance, owner=None):
        if instance:
            return self.value.__get__(instance, owner)
        return self


class modifier(_FunctionEntryDescriptor):
    """
    """
    __slots__ = ()


class entry(_EntryDescriptor):
    """
    """
    __slots__ = ()


class preloader(_FunctionEntryDescriptor):
    """
    """
    __slots__ = ()


class postloader(_FunctionEntryDescriptor):
    """
    """
    __slots__ = ()


class overload_op(_EntryDescriptor):
    """
    """
    __slots__ = ('operator', 'side')

    def __init__(self, operator, side=elements.OperationSide.NA, value=None):
        super().__init__(value)
        self.operator = operator
        self.side = side

    def __call__(self, value):
        self.value = value


class BagBlueprints:
    """
    """
    __slots__ = ()
    _ignore = ('_raw', '_ignore')
    _raw = None

    def __init_subclass__(cls, *, use_setraw=True, ignore=None, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._raw = use_setraw
        if ignore is not None:
            cls._ignore = tuple(ignore) + BagBlueprints._ignore

    # pylint: disable=too-complex
    def __new__(cls):
        args, kwargs = cls.bag_args()
        kwargs.setdefault('raw', cls._raw)
        self = cls.bag_class()(*args, **kwargs)
        for name in dir(cls):
            if name.startswith('__') and name.endswith('__') or name in cls._ignore:
                continue
            if name.endswith('_'):
                name = name[:-1]
            if not name.startswith('_'):
                name = name.replace('_', '-')
            value = getattr(cls, name)
            if isinstance(value, BagBlueprints):
                value = value()
            if name in _SPECIAL_OP_METHOD_NAMES:
                getattr(self, name)(value.value)
            elif isinstance(value, entry):
                self.add_entry(name, value.value, is_property=True)
            elif isinstance(value, modifier):
                self.add_entry(name, value.value, is_property=False)
            elif isinstance(value, preloader):
                self.preloader(value.value)
            elif isinstance(value, postloader):
                self.postloader(value.value)
            elif isinstance(value, overload_op):
                self.overload_operator(value.operator, value.side)(value.value)
        return self

    @classmethod
    def bag_class(cls):
        """
        """
        return DeferredBag

    @classmethod
    def bag_args(cls):
        """
        """
        return (), {}


class LibraryBlueprintsMeta(type):
    """
    """

    @property
    def name(cls):
        """
        """
        return cls._name

    @property
    def isolate(cls):
        """
        """
        return cls._isolate


class LibraryBlueprints(BagBlueprints, metaclass=LibraryBlueprintsMeta):
    """
    """
    __slots__ = ()
    _ignore = ('_name', '_isolate') + BagBlueprints._ignore
    _name = _isolate = None

    def __init_subclass__(cls, *, name, isolate=False, ignore=None, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._name = name
        cls._isolate = isolate
        if ignore is not None:
            cls._ignore = tuple(ignore) + LibraryBlueprints._ignore

    @classmethod
    def bag_class(cls):
        """
        """
        return DeferredPythonBasedLibrary

    @classmethod
    def bag_args(cls):
        """
        """
        return (cls._name,), {'isolate': cls._isolate}


PythonBasedLibrary.register(LibraryBlueprints)
