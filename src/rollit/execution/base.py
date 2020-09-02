"""
"""

__all__ = ['DEFAULT_SEARCH_PATH', 'NoSubject']

DEFAULT_SEARCH_PATH = ('.',)
""" """


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
