"""
"""

from ..langref import ATOM_TYPES

__all__ = ['DEFAULT_SEARCH_PATHS', 'is_atom']

DEFAULT_SEARCH_PATHS = ('.',)
""" """


def is_atom(value):
    """
    """
    return isinstance(value, ATOM_TYPES)
