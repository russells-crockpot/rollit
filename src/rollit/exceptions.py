"""
"""

__all__ = [
    'RollItException',
    'InvalidNameError',
]


class RollItException(Exception):
    """
    """


class ParsingError(RollItException, ValueError):
    """
    """


class InvalidReferenceError(ParsingError):
    """
    """


class InvalidNameError(RollItException, LookupError):
    """
    """
