"""
"""
from .base import PythonBag, PythonBasedLibrary

__all__ = [
    'AccretionPythonBasedLibrary',
]


class AccretionPythonBasedLibrary(PythonBag, PythonBasedLibrary):
    """
    """
    name = None
    """ """

    def __init__(self, name, entries=None):
        super().__init__(entries=entries)
        self.name = name

    @property
    def isolate(self):
        """
        """
        return False
