"""
"""
from collections import namedtuple

from .base import ModelElement, SingleValueElement


class TemporaryInternalElement(ModelElement):
    """
    """

    def __new__(cls, *args, **kwargs):
        kwargs.setdefault('codeinfo', None)
        return super().__new__(cls, *args, **kwargs)


class TemporarySingleValueInternalElement(SingleValueElement):
    """
    """

    def __new__(cls, *args, **kwargs):
        kwargs.setdefault('codeinfo', None)
        return super().__new__(cls, *args, **kwargs)


TemporaryInternalElement.register(TemporarySingleValueInternalElement)


def create_temporay_element_type(name, attrs=()):
    """
    """
    if not attrs:
        bases = (TemporarySingleValueInternalElement,)
    else:
        if 'codeinfo' not in attrs:
            attrs = tuple((*attrs, 'codeinfo'))
        bases = (namedtuple(f'_{name}Base', attrs), TemporaryInternalElement)
    return type(name, bases, {})


PredicatedStatement = create_temporay_element_type('PredicatedStatement',
                                                   ('predicate', 'statement'))
""" """
Otherwise = create_temporay_element_type('Otherwise')
""" """
LoopName = create_temporay_element_type('LoopName')
""" """
LoopBody = create_temporay_element_type('LoopBody')
""" """
Always = create_temporay_element_type('Always')
""" """
BagInfo = create_temporay_element_type('BagInfo', ('parent', 'isolate'))
""" """


class ItemList(tuple):
    """
    """

    def __str__(self):
        return f'{type(self).__name__}{super().__str__()}'

    def __repr__(self):
        return f'{type(self).__name__}{super().__repr__()}'

    def _asdict(self):
        return {'values': tuple(self)}

    def __bool__(self):
        return True


TemporaryInternalElement.register(ItemList)
