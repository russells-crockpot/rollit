"""
"""
import re

from pygments.lexer import RegexLexer, words, bygroups, include
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Whitespace

from ..langref import KEYWORDS, OPERATORS, SPECIAL_REFERENCES, SPECIAL_ACCESSORS

__all__ = ['RollitLexer']

basic_ops = (re.escape(op) for op in OPERATORS if op not in OPERATORS.words)


class RollitLexer(RegexLexer):
    """
    """

    name = 'rollit'
    aliases = ['Rollit']
    filenames = ['*.rollit', '*.ri']
    mimetypes = ['application/x-rollit']
    flags = re.MULTILINE | re.UNICODE
    _special_refs = f'[{"".join(re.escape(r) for r in SPECIAL_REFERENCES)}]'
    _special_accessors = f'[{"".join(re.escape(a) for a in SPECIAL_ACCESSORS)}]'

    tokens = {
        'root': [
            (r'#!.*?$', Comment.Preproc),
            include('common'),
        ],
        'ignore': [
            (r'\|', Punctuation),
            ('%>', Punctuation),
            (r'[\s\n\r\f]+', Whitespace),
            (r'//.*?$', Comment.Single),
        ],
        'common': [
            (r'-?\d*\.\d+', Number.Float),
            (r'-?\d+', Number.Integer),
            (_special_refs, Keyword.Constant),
            (words(KEYWORDS.load, suffix=r'\b'), Keyword.Namespace),
            (words(KEYWORDS, suffix=r'\b'), Name.Builtin),
            (r'\s*(<-)(?:\s*)', bygroups(Operator, Text), 'modifier_params'),
            (r'\{', Punctuation, 'reduce'),
            (r"'", String, 'string'),
            (words(basic_ops, suffix=r'\b'), Operator),
            (words(OPERATORS.words, suffix=r'\b'), Operator.Word),
            (r'[|\(\),]', Punctuation),
            ('%>', Punctuation),
            (r'[\s\n\r\f]+', Text),
            include('ignore'),
            # (r'(->)([])', ),
            # (r'(for)\s*(every)\s*(\S+)\s*that', ),
            # (r'', ),
        ],
        'reduce': [
            (r'\s*(' + _special_refs + r')\s*(\})', bygroups(Keyword.Constant,
                                                             Punctuation), '#pop'),
            (r'\}', Punctuation, '#pop'),
            include('common'),
            include('ignore'),
        ],
        'modifier_params': [
            (r'([:\[])(?:\s*)', Punctuation, 'modifier_def'),
            (',', Punctuation),
            ('[a-zA-Z_][a-zA-Z_0-9]*', Name.Variable),
            include('ignore'),
        ],
        'modifier_def': [
            #FIXME pop twice?
            (r'[\r\n\f|]', Text, '#pop'),
            include('common'),
            include('ignore'),
        ],
        'string': [
            (r"\\[\\runftvb']", String.Escapse),
            (r"[^']+", String),
            (r"'", String, '#pop'),
        ],
    }
