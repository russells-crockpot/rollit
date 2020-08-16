"""
"""
from collections import namedtuple
from .transformer import RollWithItTransformer
from ._parser import Lark_StandAlone

__all__ = ['Parser', 'parse']


class Parser:
    """
    """
    __slots__ = ('_lark_parser',)

    def __init__(self):
        self._lark_parser = Lark_StandAlone(transformer=RollWithItTransformer())

    def parse(self, string):
        """
        """
        return self._lark_parser.parse(string)


_DEFAULT_PARSER = Parser()

parse = _DEFAULT_PARSER.parse
""" """
