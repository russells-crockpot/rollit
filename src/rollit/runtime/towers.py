"""Contains dice towers. Dice towers are used to generate the random numbers for rolls.
"""
import random  # nosec
from abc import ABCMeta, abstractmethod

__all__ = [
    'DiceTower',
    'DefaultTower',
    'IncrementalTower',
    'MaxTower',
    'MinTower',
]


class DiceTower(metaclass=ABCMeta):
    """
    """

    def __call__(self, sides):
        return self.roll(sides)

    @abstractmethod
    def roll(self, sides):
        """
        """


class DefaultTower(DiceTower):
    """
    """

    def roll(self, sides):
        return random.randint(1, sides)  # nosec


class IncrementalTower(DiceTower):
    """A dice tower that instead of generating a random number, it increments an internal counter
    every time it's rolled. When a new roll is requested, the following formula is used:

    >>> ((counter + sides) % sides) + 1

    This is useful for things like testing, when you want a predictable but diverse set of numbers.
    """

    def __init__(self):
        # start at -1 because we increment BEFORE we return the value
        self.__counter = -1

    def roll(self, sides):
        self.__counter += 1
        return ((self.__counter + sides) % sides) + 1


class MaxTower(DiceTower):
    """A tower that always returns the maximum (i.e. the number of sides).
    Useful for testing.
    """

    def roll(self, sides):
        return sides


class MinTower(DiceTower):
    """A tower that always returns the minimum (i.e. 1).
    Useful for testing.
    """

    def roll(self, sides):
        return 1
