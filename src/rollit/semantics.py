"""
"""
import inspect
from collections import namedtuple
from collections.abc import Mapping
from contextlib import suppress
from functools import lru_cache

from . import model

__all__ = ['RollItSemantics']

_STATEMENT_ENDS = frozenset(('\n', '\r', '|', ''))


class CreateTypeProperty(
        namedtuple('_CreateTypePropertyBase',
                   ('model_cls', 'single_value', 'defaults', 'requires'))):
    """
    """

    def __new__(cls, model_cls, single_value=None, defaults=None, requires=()):
        if single_value is None:
            single_value = True
            if inspect.isclass(model_cls) \
                    and issubclass(model_cls, (model.ModelElement, Mapping)) \
                    and not issubclass(model_cls, model.SingleValueElement):
                single_value = False
        if single_value and requires:
            raise ValueError()
        return super().__new__(
            cls,
            model_cls=model_cls,
            single_value=single_value,
            defaults=defaults,
            requires=requires,
        )

    def __call__(self, ast):
        if self.single_value:
            if ast is None:
                ast = self.defaults
            return self.model_cls(ast)
        if not isinstance(ast, Mapping):
            return ast
        for name in self.requires:
            if name not in ast:
                return ast
        if self.defaults:
            for k, v in self.defaults.items():
                if k not in ast or ast[k] is None:
                    ast[k] = v
        return self.model_cls(**ast)


class LruCachedCreateTypeProperty(CreateTypeProperty):
    """
    """

    @lru_cache
    def __call__(self, ast):
        return super().__call__(ast)


# pylint: disable=missing-function-docstring
class RollItSemantics:
    """
    """
    _in_modifier_def = False
    _name_not_ref = False

    for_every_body = CreateTypeProperty(model.ForEvery, False, {'name': None})
    use_if = CreateTypeProperty(model.UseIf, False, requires=('use', 'predicate', 'otherwise'))
    enlarge = CreateTypeProperty(model.Enlarge, False)
    roll_math = CreateTypeProperty(model.BinaryOp, False, requires=('left', 'op', 'right'))
    math = CreateTypeProperty(model.BinaryOp, False, requires=('left', 'op', 'right'))
    comparison = CreateTypeProperty(model.BinaryOp, False, requires=('left', 'op', 'right'))
    dice = CreateTypeProperty(model.Dice, False, requires=('number_of_dice', 'sides'))
    access = CreateTypeProperty(model.Access, False)
    access_expr = CreateTypeProperty(model.Access, False, requires=('accessing', 'accessors'))
    int = LruCachedCreateTypeProperty(int, True)
    float = LruCachedCreateTypeProperty(float, True)

    #@lru_cache
    def conditional(self, ast):
        if not isinstance(ast, model.ModelElement) and isinstance(ast, tuple) \
                and len(ast) > 1 and ast[0] == 'not':
            return self._negate(ast[1])
        return ast

    @lru_cache
    def name(self, ast):
        with suppress(ValueError):
            return model.SpecialReference(ast)
        return ast

    #@lru_cache
    def assignment(self, ast):
        target = ast['target']
        if ast['op'] == '=':
            return model.Assignment(target=target, value=ast['value'])
        op = ast['op'][:-1]
        return model.Assignment(
            target=target,
            value=model.BinaryOp(left=target, op=op, right=ast['value']),
        )

    def modify(self, ast):
        if not isinstance(ast, dict) or 'subject' not in ast or 'modifier' not in ast:
            return ast
        subject = ast['subject']
        call = model.ModifierCall(modifier=ast['modifier'], args=ast.get('args', ()))
        if isinstance(subject, model.Modify):
            return model.Modify(subject=subject.subject, modifiers=subject.modifiers + (call,))
        return model.Modify(subject=subject, modifiers=(call,))

    def load_body(self, ast):
        if ast['to_load'] == '!':
            return tuple(model.CreateBag(target) for target in ast['into'])
        if ast['to_load'] == '*':
            return tuple(
                model.Load(
                    to_load=model.SpecialReference.ALL,
                    load_from=child,
                    into=ast.get('into', model.SpecialReference.ROOT),
                ) for child in ast['load_from'])
        if not ast['to_load']:
            return tuple(
                model.Load(
                    to_load=model.SpecialReference.ALL,
                    load_from=child,
                    into=ast.get('into', child),
                ) for child in ast['load_from'])
        return tuple(
            model.Load(
                to_load=child,
                load_from=ast.get('load_from'),
                into=ast.get('into', child),
            ) for child in ast['to_load'])

    #@lru_cache
    def statement(self, ast):
        if isinstance(ast, str) and ast in _STATEMENT_ENDS:
            return None
        return ast

    #@lru_cache
    def if_body(self, ast):
        rval = model.If(predicate=ast['predicate'],
                        then=ast['then'],
                        otherwise=ast.get('otherwise'))
        if ast['unless']:
            previous = None
            for unless in ast['unless']:
                previous = model.If(predicate=unless['predicate'],
                                    then=unless['then'],
                                    otherwise=previous)
            rval = model.If(
                predicate=self._negate(ast['predicate']),
                then=previous,
                otherwise=rval,
            )
        return rval

    @staticmethod
    def _negate(element):
        return element.value if isinstance(element, model.Negation) else model.Negation(element)

    #@lru_cache
    def until_do_body(self, ast):
        ast.setdefault('name', None)
        ast.setdefault('otherwise', None)
        do = ast.pop('do')
        if 'except_when' in ast:
            for _, _, ew_predicate, _, ew_then in ast.pop('except_when'):
                do = model.If(predicate=ew_predicate, then=ew_then, otherwise=do)
        ast['do'] = do
        return model.UntilDo(**ast)

    #@lru_cache
    def enlarge_reduce(self, ast):
        if isinstance(ast, model.Enlarge):
            return ast
        if not ast:
            ast = model.SpecialReference.NONE
        elif ast == '*':
            ast = model.SpecialReference.ALL
        return model.Reduce(ast)

    #@lru_cache
    def length(self, ast):
        if isinstance(ast, tuple) and not isinstance(ast, model.ModelElement) \
                and len(ast) == 2 and ast[0] == '#':
            return model.Length(ast[1])
        return ast

    #@lru_cache
    def modifier_call(self, ast):
        if ast['args'] is None:
            ast['args'] = ()
        return model.ModifierCall(**ast)

    #@lru_cache
    def restart_body(self, ast):
        specifier = model.RestartLocationSpecifier(ast['location_specifier'])
        target = ast.get('target', '!')
        if target in ('~', '!'):
            target = 'NONE' if target == '!' else 'ROOT'
            # pylint: disable=protected-access
            return getattr(model.Restart, f'{specifier._name_}_{target}')
        return model.Restart(location_specifier=specifier, target=target)

    def _modifier_def(self, ast):
        return model.ModifierDef(
            target=ast['target'],
            parameters=ast['parameters'] or (),
            definition=ast['definition'] or (),
        )

    #@lru_cache
    def basic_statement(self, ast):
        if ast == 'leave':
            return model.SingleWordStatment.LEAVE
        if not isinstance(ast, model.ModelElement):
            if isinstance(ast, Mapping):
                with suppress(TypeError, LookupError):
                    if len(ast) == 3 and 'op' in ast and ast['op'][-1] == '=' and ast['op'] != '==':
                        return self.assignment(ast)
                    return self._modifier_def(ast)
            elif isinstance(ast, (list, tuple)):
                with suppress(IndexError):
                    if ast[0] == 'restart':
                        return ast[1]
        return ast
