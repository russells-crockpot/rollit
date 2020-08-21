"""
"""
import builtins
import re
from collections.abc import Mapping
from contextlib import suppress

from . import model

__all__ = ['RollItSemantics']

STATMENTS_END_PAT = re.compile(r'[\r\n\|]')


# pylint: disable=missing-function-docstring
class RollItSemantics:
    """
    """
    _in_modifier_def = False
    _name_not_ref = False

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
            if issubclass(model_cls, model.SingletonElement):
                return model_cls(ast)
            if isinstance(ast, Mapping):
                return model_cls(**ast)
        return ast

    def conditional(self, ast, *args, **kwargs):
        if not isinstance(ast, model.ModelElement) and isinstance(ast, tuple) \
                and len(ast) > 1 and ast[0] == 'not':
            return model.Negation(ast[1])
        return self._default(ast, *args, **kwargs)

    def modifier_def(self, ast, *args, **kwargs):
        target = ast['target']
        parameters = ast['parameters'] or ()
        definition = ast['definition'] or ()
        if isinstance(target, model.Reference):
            target = target.value
        parameters = tuple(p.value if isinstance(p, model.Reference) else p for p in parameters)
        return model.ModifierDef(
            target=target,
            parameters=parameters,
            definition=definition,
        )

    def reference(self, ast, *args, **kwargs):
        # if not self._in_modifier_def and ast == '?':
        #     raise InvalidReferenceError('"?" cannot be used outside of a modifier definition!')
        if self._name_not_ref:
            return ast
        return model.Reference(ast)

    #FIXME Handle accesses
    def _assigment(self, ast):
        target = ast['target']
        if ast['op'] == '=':
            if isinstance(target, model.Reference):
                target = target.value
            return model.Assignment(target=target, value=ast['value'])
        if not isinstance(target, model.Reference):
            target = model.Reference(target)
        op = ast['op'][:-1]
        value_cls = model.RollMath if op in ('&', '^') else model.Math
        return model.Assignment(target=target.value,
                                value=value_cls(left=target, op=op, right=ast['value']))

    def load_body(self, ast, *args, **kwargs):
        if 'from_dialect' not in ast:
            items = []
            into = ast.get('into')
            for child in ast.pop('to_load'):
                items.append(
                    self.load_body(
                        dict(
                            from_dialect=child,
                            to_load=model.SpecialReference.ALL,
                            into=into or model.Reference(child),
                        )))
            if len(items) == 1:
                return items[0]
            return items
        ast.setdefault('into', model.SpecialReference.ROOT)
        return model.Load(**ast)

    def statement(self, ast, *args, **kwargs):
        if isinstance(ast, str) and not (ast and STATMENTS_END_PAT.sub('', ast)):
            return None
        return self._default(ast, *args, **kwargs)

    def if_body(self, ast, *args, **kwargs):
        rval = model.If(predicate=ast['predicate'],
                        then=ast['then'],
                        otherwise=ast.get('otherwise'))
        for unless in ast['unless']:
            rval = model.If(predicate=unless['predicate'], then=unless['then'], otherwise=rval)
        return rval

    def _replace_do_body(self, ast):
        ast.setdefault('otherwise', None)
        if 'except_when' not in ast:
            return
        rval = ast.pop('do')
        for except_when in ast.pop('except_when'):
            rval = model.If(predicate=except_when.predicate, then=except_when.then, otherwise=rval)
        ast['do'] = rval

    def do_until_body(self, ast, *args, **kwargs):
        self._replace_do_body(ast)
        return (
            ast['do'],
            model.UntilDo(**ast),
        )

    def until_do_body(self, ast, *args, **kwargs):
        self._replace_do_body(ast)
        return model.UntilDo(**ast)

    def enlarge(self, ast, *args, **kwargs):
        return model.Enlarge(**ast)

    def reduce_enlarge(self, ast, *args, **kwargs):
        if isinstance(ast, model.Enlarge):
            return ast
        if not ast:
            ast = model.SpecialReference.NONE
        elif ast == '*':
            ast = model.SpecialReference.ALL
        return model.Reduce(ast)

    def length(self, ast, *args, **kwargs):
        if isinstance(ast, tuple) and not isinstance(ast, model.ModelElement) \
                and len(ast) == 2 and ast[0] == '#':
            return model.Length(ast[1])
        return ast

    def modifier_call(self, ast, *args, **kwargs):
        if ast['args'] is None:
            ast['args'] = ()
        return model.ModifierCall(**ast)

    def basic_statement(self, ast, *args, **kwargs):
        if ast == 'skip':
            return model.FlowControlConstant.SKIP
        if ast == 'stop':
            return model.FlowControlConstant.STOP
        with suppress(TypeError):
            if len(ast) == 3 and 'op' in ast \
                    and ast['op'][-1] == '=' and ast['op'] != '==':
                return self._assigment(ast)
        return self._default(ast, *args, **kwargs)
