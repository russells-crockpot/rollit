"""
"""
import builtins
from collections.abc import Mapping
from contextlib import suppress

from . import model

__all__ = ['RollItSemantics']


# pylint: disable=missing-function-docstring
class RollItSemantics:
    """
    """

    def _default(self, ast, model_cls=None):
        if not model_cls:
            with suppress(TypeError):
                if '_type' in ast:
                    model_cls = ast.pop('_type')
        if model_cls and model_cls != 'IGNORE' and not isinstance(ast, model.ModelElement):
            module = model
            if model_cls.startswith('pybuiltin_'):
                return getattr(builtins, model_cls.replace('pybuiltin_', '', 1))(ast)
            model_cls = getattr(module, model_cls)
            if (ast is None and model_cls.accepts_none) or model_cls.singleton:
                return model_cls(ast)
            if isinstance(ast, Mapping):
                return model_cls(**ast)
        if isinstance(ast, str) and ast in model.STATEMENT_KEYWORDS:
            return model.STATEMENT_KEYWORDS[ast]
        return ast

    def conditional(self, ast, *args, **kwargs):
        if not isinstance(ast, model.ModelElement) and isinstance(ast, tuple) \
                and len(ast) > 1 and ast[0] == 'not':
            return model.Negation(ast[1])
        return self._default(ast, *args, **kwargs)
