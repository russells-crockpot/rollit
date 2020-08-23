"""
"""
from abc import ABCMeta, abstractmethod
from collections import namedtuple

__all__ = []


class Reducable(metaclass=ABCMeta):
    """
    """
    __slots__ = ()

    @abstractmethod
    def reduce(self, context):
        """
        """


class Runnable(metaclass=ABCMeta):
    """
    """
    __slots__ = ()

    @abstractmethod
    def run(self, context):
        """
        """


class Roll(list, Reducable):
    """
    """

    def __init__(self, results):
        super().__init__(results)
        self._value = None

    @property
    def total(self):
        """
        """
        return sum(self)

    @property
    def value(self):
        """
        """
        if self._value is None:
            return self.total
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def reduce(self, context):
        return self.value
