"""
"""

__all__ = [
    'RollWithItException',
    'InvalidNameError',
]


class RollWithItException(Exception):
    """
    """


class InvalidNameError(RollWithItException, LookupError):
    """
    """
