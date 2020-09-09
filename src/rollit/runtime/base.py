"""
"""
import contextvars

from ..langref import ATOM_TYPES

__all__ = ['DEFAULT_SEARCH_PATHS', 'is_atom', 'context']

DEFAULT_SEARCH_PATHS = ('.',)
""" """

_CURRENT_CONTEXT = contextvars.ContextVar('current-runtime-context', default=None)


def is_atom(value):
    """
    """
    return isinstance(value, ATOM_TYPES)


class _CurrentContextProxy:
    __slots__ = ()
    __getattr__ = lambda s, n: getattr(_CURRENT_CONTEXT.get(), n)
    __setattr__ = lambda s, n, v: setattr(_CURRENT_CONTEXT.get(), n, v)
    __delattr__ = lambda s, n: delattr(_CURRENT_CONTEXT.get(), n)
    __getitem__ = lambda s, n: _CURRENT_CONTEXT.get().__getitem__(n)
    __setitem__ = lambda s, n, v: _CURRENT_CONTEXT.get().__setitem__(n, v)
    __delitem__ = lambda s, n: _CURRENT_CONTEXT.get().__delitem__(n)
    __enter__ = lambda s: _CURRENT_CONTEXT.get().__enter__()
    __exit__ = lambda s: _CURRENT_CONTEXT.get().__exit__()
    __contains__ = lambda s, n: _CURRENT_CONTEXT.get().__contains__(n)
    __dir__ = lambda s: dir(_CURRENT_CONTEXT.get())
    __call__ = lambda s, v: _CURRENT_CONTEXT.get()(v)


context = _CurrentContextProxy()
"""The current runtime context
"""

del _CurrentContextProxy
