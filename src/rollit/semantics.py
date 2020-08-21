"""
"""
import inspect
import re
from collections import namedtuple
from collections.abc import Mapping
from contextlib import suppress

from . import model
from .exceptions import ParsingError

__all__ = ['RollItSemantics']

STATMENTS_END_PAT = re.compile(r'[\r\n\|]')


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

    def __call__(self, ast, *args, **kwargs):
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


# pylint: disable=missing-function-docstring
class RollItSemantics:
    """
    """
    _in_modifier_def = False
    _name_not_ref = False

    for_every_body = CreateTypeProperty(model.ForEvery, False, {'name': None})
    use_if = CreateTypeProperty(model.UseIf, False, requires=('use', 'predicate', 'otherwise'))
    enlarge = CreateTypeProperty(model.Enlarge, False)
    roll_math = CreateTypeProperty(model.RollMath, False, requires=('left', 'op', 'right'))
    math = CreateTypeProperty(model.Math, False, requires=('left', 'op', 'right'))
    comparison = CreateTypeProperty(model.Comparison, False, requires=('left', 'op', 'right'))
    dice = CreateTypeProperty(model.Dice, False, requires=('number_of_dice', 'sides'))
    access = CreateTypeProperty(model.Access, False, requires=('accessing', 'accessors'))
    modify = CreateTypeProperty(model.Modify, False, requires=('subject', 'modifiers'))
    modifier_def = CreateTypeProperty(model.ModifierDef,
                                      False,
                                      defaults=dict(parameters=(), definition=()))
    int = CreateTypeProperty(int, True)
    float = CreateTypeProperty(float, True)

    def conditional(self, ast, *args, **kwargs):
        if not isinstance(ast, model.ModelElement) and isinstance(ast, tuple) \
                and len(ast) > 1 and ast[0] == 'not':
            return model.Negation(ast[1])
        return ast

    def name(self, ast):
        with suppress(ValueError):
            return model.SpecialReference(ast)
        return ast

    #FIXME Handle accesses
    def _assigment(self, ast):
        target = ast['target']
        if ast['op'] == '=':
            return model.Assignment(target=target, value=ast['value'])
        op = ast['op'][:-1]
        value_cls = model.RollMath if op in ('&', '^') else model.Math
        return model.Assignment(target=target,
                                value=value_cls(left=target, op=op, right=ast['value']))

    def load_body(self, ast):
        if 'from_dialect' not in ast:
            if '*' in ast['to_load']:
                raise ParsingError('Cannot load "all (*)" of nothing.')
            items = []
            into = ast.get('into')
            for child in ast.pop('to_load'):
                items.append(
                    self.load_body(
                        dict(
                            from_dialect=child,
                            to_load=model.SpecialReference.ALL,
                            into=into or child,
                        )))
            if len(items) == 1:
                return items[0]
            return items
        with suppress(TypeError):
            if '*' in ast['to_load']:
                if len(ast['to_load']) > 1:
                    raise ParsingError('Loading * loads everything, other values cannot be '
                                       'specified.')
                del ast['to_load']
                ast['to_load'] = model.SpecialReference.ALL
        ast.setdefault('into', model.SpecialReference.ROOT)
        return model.Load(**ast)

    def statement(self, ast, *args, **kwargs):
        if isinstance(ast, str) and not (ast and STATMENTS_END_PAT.sub('', ast)):
            return None
        return ast

    #FIXME Unlesses need to have a negation of the initial if predicate anded to them
    def if_body(self, ast, *args, **kwargs):
        rval = model.If(predicate=ast['predicate'],
                        then=ast['then'],
                        otherwise=ast.get('otherwise'))
        for unless in ast['unless']:
            rval = model.If(predicate=unless['predicate'], then=unless['then'], otherwise=rval)
        return rval

    @staticmethod
    def _negate(element):
        return element.value if isinstance(element, model.Negation) else model.Negation(element)

    def until_do_body(self, ast, *args, **kwargs):
        ast.setdefault('name', None)
        ast.setdefault('otherwise', None)
        do = ast.pop('do')
        if 'except_when' in ast:
            for _, _, ew_predicate, _, ew_then in ast.pop('except_when'):
                do = model.If(predicate=ew_predicate, then=ew_then, otherwise=do)
        ast['do'] = do
        return model.UntilDo(**ast)

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

    def restart_body(self, ast):
        specifier = model.RestartLocationSpecifier(ast['location_specifier'])
        target = ast.get('target', '!')
        if target in ('~', '!'):
            target = 'NONE' if target == '!' else 'ROOT'
            # pylint: disable=protected-access
            return getattr(model.Restart, f'{specifier._name_}_{target}')
        return model.Restart(location_specifier=specifier, target=target)

    def basic_statement(self, ast, *args, **kwargs):
        if ast == 'leave':
            return model.SingleWordStatment.LEAVE
        if not isinstance(ast, model.ModelElement):
            if isinstance(ast, Mapping):
                with suppress(TypeError, LookupError):
                    if len(ast) == 3 and 'op' and ast['op'][-1] == '=' and ast['op'] != '==':
                        return self._assigment(ast)
            elif isinstance(ast, (list, tuple)):
                with suppress(IndexError):
                    if ast[0] == 'restart':
                        return ast[1]
        return ast
