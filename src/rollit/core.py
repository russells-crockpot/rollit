"""
"""

from .transformer import RollWithItTransformer
from .dialect import Dialect
from .dialects.default import dialect as default_dialect
from .ast import DiceRoll, RollResults
from .parser import Parser

__all__ = []


class Context:
    """
    """
    root_dialect = None
    """ """
    current_dialect = None
    """ """

    def __init__(self, root_dialect=default_dialect):
        if not root_dialect:
            root_dialect = Dialect(is_root=True)
        else:
            root_dialect = root_dialect.child(root_dialect.name, is_root=True, holder={})
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
        return self.root_dialect.get_dialect(name)


class Session:
    """
    """

    _parser = Parser()
