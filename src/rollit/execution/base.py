"""
"""
from contextlib import contextmanager, nullcontext

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


# pylint: disable=protected-access
@contextmanager
def now_access(context, accessing):
    """
    """
    if context._accessing != accessing:
        old_accessing = context._accessing
        context._accessing = accessing
        yield
        context._accessing = old_accessing
    else:
        yield


# pylint: disable=protected-access
@contextmanager
def with_child_scope(context, obj):
    """
    """
    if obj.__specs__.new_scope:
        context._scope = context.scope.child(isolated=obj.__specs__.isolate_scope)
        yield
        old_scope = context.scope
        context._scope = context.scope.parent
        if not obj.__specs__.retain_scope:
            old_scope.destroy()
            del old_scope
    else:
        yield


def adjust_accessing(context, obj):
    """
    """
    if obj.__specs__.always_use_scope:
        return now_access(context, context._scope)
    if obj.__specs__.new_scope:
        return now_access(context, obj)
    return nullcontext()
