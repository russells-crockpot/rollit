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
        if not isinstance(ast, model.ModelElement) and model_cls and model_cls != 'IGNORE':
            module = model
            if model_cls.startswith('pybuiltin_'):
                return getattr(builtins, model_cls.replace('pybuiltin_', '', 1))(ast)
            model_cls = getattr(module, model_cls)
            with suppress(TypeError):
                if (ast is None and model_cls.accepts_none) or model_cls.singleton:
                    # cp.green(f'{model_cls=}')
                    # cp.yellow(f'{ast=}')
                    # cp.red(f'{model_cls=}')
                    rval = model_cls(ast)
                    # cp.cyan(f'{rval=}')
                    # cp.magenta(f'{type(rval)=}')
                    return rval
                # cp.green(f'{model_cls=}')
                # cp.yellow(f'{ast=}')
                # cp.red(f'{model_cls=}')
                rval = model_cls(**ast)
                # cp.cyan(f'{rval=}')
                # cp.magenta(f'{type(rval)=}')
                return rval
        return ast
