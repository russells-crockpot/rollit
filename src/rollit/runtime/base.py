"""
"""
import contextvars

from ..langref import ATOM_TYPES

__all__ = ['is_atom', 'context']

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
    __str__ = lambda s: _CURRENT_CONTEXT.get().__str__()
    __repr__ = lambda s: _CURRENT_CONTEXT.get().__repr__()
    __bool__ = lambda s: _CURRENT_CONTEXT.get() is not None


context = _CurrentContextProxy()
"""The current :class:`~rollit.runtime.core.RuntimeContext`.
"""

del _CurrentContextProxy
