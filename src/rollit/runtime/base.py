"""
"""

from ..langref import ATOM_TYPES

__all__ = ['DEFAULT_SEARCH_PATHS', 'NoSubject', 'NoValue', 'is_atom']

DEFAULT_SEARCH_PATHS = ('.',)
""" """


def __create_no_value():

    class _NoValueBase(tuple):
        __the_object = None

        def __new__(cls):
            if not cls.__the_object:
                cls.__the_object = super().__new__(cls)
            return cls.__the_object

        def __bool__(self):
            return False

        @staticmethod
        def __str__():
            return 'NoValue'

        @staticmethod
        def __repr__():
            return 'NoValue'

    return _NoValueBase()


NoValue = __create_no_value()
""" """
del __create_no_value


def __create_no_subject():

    class _NoSubjectBase(tuple):
        __the_object = None

        def __new__(cls):
            if not cls.__the_object:
                cls.__the_object = super().__new__(cls)
            return cls.__the_object

        def __bool__(self):
            return False

        @staticmethod
        def __str__():
            return 'NoSubject'

        @staticmethod
        def __repr__():
            return 'NoSubject'

    return _NoSubjectBase()


NoSubject = __create_no_subject()
""" """
del __create_no_subject


def is_atom(value):
    """
    """
    return isinstance(value, ATOM_TYPES)
