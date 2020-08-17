"""
"""
from contextlib import suppress

from .dialect import Dialect
from .dialects.default import dialect as default_dialect
from .exceptions import InvalidNameError
from .parser import Parser

__all__ = [
    'Session',
    'ExecutionContext',
]


class ExecutionContext:
    """
    """
    root_dialect = None
    """ """
    current_dialect = None
    """ """

    def __init__(self, root_dialect):
        self._dialect_holder = {}
        if not root_dialect:
            root_dialect = Dialect(is_root=True, holder=self._dialect_holder)
        else:
            root_dialect = root_dialect.child(root_dialect.name,
                                              is_root=True,
                                              holder=self._dialect_holder)
        self.current_dialect = self.root_dialect = root_dialect

    def get_dialect(self, name):
        """
        """
        if not name:
            return None
        if name == '^':
            if not self.current_dialect.parent:
                raise Exception()
            return self.current_dialect.parent
        if name == '~':
            return self.root_dialect
        if name not in self._dialect_holder:
            raise InvalidNameError()
        return self._dialect_holder[name]

    def get_or_create_dialect(self, name, parent):
        """
        """
        if isinstance(parent, str):
            parent = self.get_dialect(parent)
        if name:
            with suppress(InvalidNameError):
                dialect = self.get_dialect(name)
                if dialect.parent != parent:
                    #TODO
                    raise ValueError()
                return dialect
        return Dialect(name, parent, holder=self._dialect_holder)


class Session:
    """
    """

    _parser = Parser()

    def __init__(self, root_dialect=default_dialect):
        self._context = ExecutionContext(root_dialect)
