"""
"""
import enum
from collections import namedtuple
from contextlib import suppress

from .base import (ElementSpecs, ModelEnumElement, ModelElement, SingleValueElement,
                   ConstantElement, PredicatedElementMixIn)
from ..util import is_valid_iterable

__all__ = [
    'create_model_element_type',
    'Access',
    'Assignment',
    'Attempt',
    'BinaryOp',
    'ButIf',
    'ClearValue',
    'DiceNode',
    'Enlarge',
    'ForEvery',
    'IfThen',
    'Leave',
    'Load',
    'ModifierCall',
    'ModifierDef',
    'Modify',
    'Negation',
    'NewBag',
    'Oops',
    'OverloadOperator',
    'Reduce',
    'Restart',
    'RestartLocationSpecifier',
    'SpecialAccessor',
    'SpecialReference',
    'StringLiteral',
    'UntilDo',
    'UseIf',
]


def create_model_element_type(name,
                              attrs=(),
                              constant=False,
                              specs=ElementSpecs(),
                              *,
                              basic_predicated=False):
    """
    """
    class_attrs = {}
    if basic_predicated and not specs.predicate_info:
        specs = specs._replace(predicate_info=tuple(attrs[:3]))
    if constant:
        bases = (ConstantElement,)
    elif not attrs:
        bases = (SingleValueElement,)
    else:
        if 'codeinfo' not in attrs:
            attrs = tuple((*attrs, 'codeinfo'))
        if specs.predicate_info:
            bases = (PredicatedElementMixIn, namedtuple(f'_{name}Base', attrs), ModelElement)
        else:
            bases = (namedtuple(f'_{name}Base', attrs), ModelElement)
    class_attrs.setdefault('__specs__', specs)
    return type(name, bases, class_attrs)


class Operator(ModelEnumElement):
    """
    """


class OneSidedOperator(Operator):
    """
    """
    _ignore_ = ('python_name',)
    python_name = None

    EQUALS = ('==', 'equals')
    NOT_EQUALS = ('!=', 'not_equals')
    GREATER_THAN_EQUALS = ('<=', 'greater_than_equals')
    LESS_THAN_EQUALS = ('>=', 'less_than_equals')
    LESS_THAN = ('<', 'less_than')
    GREATER_THAN = ('>', 'greater_than')
    HAS = ('has', 'has')

    def __new__(cls, value, python_name):
        self = object.__new__(cls)
        self._value_ = value
        self.python_name = python_name
        return self


class TwoSidedOperator(Operator):
    """
    """
    _ignore_ = ('left_python_name', 'right_python_name')
    left_python_name = right_python_name = None

    # Two sided
    MULTIPLY = ('*', 'l_multiply', 'r_multiply')
    TRUEDIV = ('%/', 'l_truediv', 'r_truediv')
    FLOORDIV = ('/', 'l_floordiv', 'r_floordiv')
    MODULO = ('%', 'l_modulo', 'r_modulo')
    ADD = ('+', 'l_add', 'r_add')
    SUBTRACT = ('-', 'l_subtract', 'r_subtract')
    OR = ('or', 'l_or', 'r_or')
    AND = ('and', 'l_and', 'r_and')
    ISA = ('isa', 'l_isa', 'r_isa')
    EXPAND = ('@', 'l_expand', 'r_expand')
    AMPERSAND = ('&', 'l_ampersand', 'r_ampersand')

    def __new__(cls, value, left_python_name, right_python_name):
        self = object.__new__(cls)
        self._value_ = value
        self.left_python_name = left_python_name
        self.right_python_name = right_python_name
        return self


class OverloadOnlyOperator(Operator):
    """
    """
    _ignore_ = ('python_name',)
    python_name = None

    LENGTH = ('#', 'length')
    REDUCE = ('{}', 'reduce')
    SUBJECT = ('?', 'as_subject')
    ITERATE = ('forevery', 'iterate')
    ISZERO = ('0', 'iszero')

    def __new__(cls, value, python_name):
        self = object.__new__(cls)
        self._value_ = value
        self.python_name = python_name
        return self


class SpecialAccessor(ModelEnumElement):
    """
    """
    LENGTH = '#'
    TOTAL = '+'
    VALUE = '='
    EVERY = '*'
    PARENT = '^'

    # pylint: disable=no-member, missing-function-docstring
    def evaluate(self, context):
        return context[self]


class SpecialEntry(ModelEnumElement):
    """
    """
    PARENT = '^'
    ACCESS = '.'
    SET = '='
    CLEAR = 'clear'
    CREATE = ':'
    DESTROY = '!'

    # pylint: disable=no-member, missing-function-docstring
    def evaluate(self, context):
        return context[self]


class SpecialReference(ModelEnumElement):
    """
    """
    SUBJECT = '?'
    ROOT = '~'
    ALL = '*'
    NONE = '!'
    LOCAL = '$'
    ERROR = '#'
    PARENT = '^'

    # pylint: disable=no-member
    def __nonzero__(self):
        return self._name_ != 'NONE'

    # pylint: disable=no-member, missing-function-docstring
    def evaluate(self, context):
        if self._name_ == 'NONE':
            return None
        return context[self._value_]

    # pylint: disable=no-member, missing-function-docstring
    @property
    def value(self):
        return self._value_


class RestartLocationSpecifier(ModelEnumElement):
    """
    """
    AT = 'at'
    BEFORE = 'before'
    AFTER = 'after'


class StringLiteral(namedtuple('_StringLiteralBase', ('parts', 'codeinfo')), ModelElement):
    """
    """
    __specs__ = ElementSpecs(intern_strings=False)

    def __new__(cls, parts, codeinfo):
        new_parts = []
        for part in parts:
            if isinstance(part, StringLiteral):
                new_parts.extend(part.parts)
            else:
                new_parts.append(part)
        return super().__new__(cls, tuple(new_parts), codeinfo=codeinfo)

    @property
    def value(self):
        """
        """
        if isinstance(self.parts, str):
            return self.parts
        if len(self.parts) == 1:
            return self.parts[0]
        return ''.join(self.parts)

    def _to_test_dict(self):
        """
        """
        return {
            '_class': type(self).__name__,
            'value': self.value,
        }

    @classmethod
    def preevaluate(cls, value):
        return value.value


SingleValueElement.register(StringLiteral)


class Reference(create_model_element_type('BaseReference')):
    """
    """

    def __new__(cls, value, *, codeinfo):
        with suppress(ValueError):
            return SpecialReference(value)
        #pylint: disable=too-many-function-args
        return super().__new__(cls, value, codeinfo=codeinfo)


Reference.register(SpecialReference)


class OperationSide(enum.Enum):
    """
    """
    NA = enum.auto()
    LEFT = enum.auto()
    RIGHT = enum.auto()


# Loops
UntilDo = create_model_element_type('UntilDo', ('name', 'until', 'do', 'otherwise'))
""" """
ForEvery = create_model_element_type('ForEvery', ('name', 'item_name', 'iterable', 'do'))
""" """
Restart = create_model_element_type('Restart', ('location_specifier', 'target'))
""" """

# Error Handling
Attempt = create_model_element_type('Attempt', ('attempt', 'buts', 'always'))
""" """
ButIf = create_model_element_type('ButIf', ('predicate', 'statement'), basic_predicated=True)
""" """
Oops = create_model_element_type('Oops')
""" """

# Modifiers
Modify = create_model_element_type('Modify', ('subject', 'modifiers'))
""" """
ModifierCall = create_model_element_type('ModifierCall', ('modifier', 'args'))
""" """
ModifierDef = create_model_element_type('ModifierDef', ('target', 'parameters', 'definition'))
""" """
Leave = create_model_element_type('Leave', constant=True)
""" """

BinaryOp = create_model_element_type('BinaryOp', ('left', 'op', 'right'))
""" """
Negation = create_model_element_type('Negation')
""" """

Assignment = create_model_element_type('Assignment', ('target', 'value'))
""" """
Load = create_model_element_type('Load', ('to_load', 'load_from', 'into'))
""" """
Access = create_model_element_type('Access', ('accessing', 'accessors'))
""" """
Enlarge = create_model_element_type('Enlarge', ('size', 'value'))
""" """
Reduce = create_model_element_type('Reduce')
""" """

NewBag = create_model_element_type('NewBag')
""" """
RawAccessor = create_model_element_type('RawAccessor')
""" """
OverloadOperator = create_model_element_type('OverloadOperator', ('operator', 'side'))
""" """
ClearValue = create_model_element_type('ClearValue')
""" """

# Predicates
UseIf = create_model_element_type('UseIf', ('use', 'predicate', 'otherwise'),
                                  specs=ElementSpecs(
                                      predicate_info=('predicate', 'use', 'otherwise'),
                                  ))
""" """

DiceNode = create_model_element_type('DiceNode', ('number_of_dice', 'sides'))
""" """


class IfThen(
        create_model_element_type('_IfThenParent', ('predicate', 'then', 'otherwise'),
                                  basic_predicated=True)):
    """ """

    def __new__(cls, predicate, then, otherwise, *, codeinfo):
        if then is None:
            then = ()
        elif not is_valid_iterable(then) or not isinstance(then, tuple):
            then = (then,)
        if otherwise is None:
            otherwise = ()
        elif not is_valid_iterable(otherwise) or not isinstance(otherwise, tuple):
            otherwise = (otherwise,)
        #pylint: disable=unexpected-keyword-arg
        return super().__new__(
            cls,
            predicate=predicate,
            then=then,
            otherwise=otherwise,
            codeinfo=codeinfo,
        )
