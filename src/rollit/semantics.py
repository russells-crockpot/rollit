"""
"""
import builtins
from contextlib import suppress

from . import model

__all__ = ['RollItSemantics']


class RollItSemantics:
    """
    """

    def _default(self, ast, model_cls=None):
        if not isinstance(ast, model.Resolvable) and model_cls and model_cls != 'IGNORE':
            module = model
            if model_cls.startswith('pybuiltin_'):
                module = builtins
                model_cls = model_cls.replace('pybuiltin_', '', 1)
            model_cls = getattr(module, model_cls)
            with suppress(TypeError):
                if isinstance(ast, str):
                    return model_cls(ast)
                return model_cls(**ast)
        return ast
