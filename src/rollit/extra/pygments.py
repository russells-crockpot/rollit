"""
"""
#pylint: skip-file
import re

from pygments.lexer import RegexLexer, include, bygroups, default, combined, \
    words
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Error, Whitespace, Other

__all__ = []


class RollitLexer(RegexLexer):
    """
    """

    name = 'rollit'
    aliases = ['RollIt']
    filenames = ['*.rollit', '*.ri']
    mimetypes = ['application/x-rollit']

    tokens = {'common': [], 'root': [], 'loop': []}
