"""
"""

from ..dialect import Dialect

__all__ = [
    'dialect',
]

dialect = Dialect('default')


@dialect.modifier
def highest(n=1, *, roll):
    """
    """
    return sorted(roll.rolls, reverse=True)[:n]


@dialect.modifier
def lowest(n=1, *, roll):
    """
    """
    return sorted(roll.rolls)[:n]


@dialect.modifier
def unique(*, roll):
    """
    """
    return set(roll.rolls)


dialect.add_alias('top', 'highest')
dialect.add_alias('bottom', 'lowest')
