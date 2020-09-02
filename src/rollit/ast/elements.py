"""
"""
from collections import namedtuple

from .base import create_model_element_type, ElementSpecs, ModelEnumElement, ModelElement, \
        SingleValueElement

__all__ = [
    'Access',
    'Assignment',
    'Attempt',
    'BinaryOp',
    'ButIf',
    'ClearValue',
    'Dice',
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
    'Reduce',
    'Restart',
    'RestartLocationSpecifier',
    'SpecialAccessor',
    'SpecialReference',
    'StringLiteral',
    'UntilDo',
    'UseIf',
]


class SpecialAccessor(ModelEnumElement):
    """
    """
    LENGTH = '#'
    TOTAL = '+'
    VALUE = '='
    EVERY = '*'

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

    def __new__(cls, *parts, codeinfo):
        return super().__new__(cls, parts, codeinfo=codeinfo)

    @property
    def value(self):
        """
        """
        if isinstance(self.parts, str):
            return self.parts
        if len(self.parts) == 1:
            return self.parts[0]
        return ''.join(self.parts)


SingleValueElement.register(StringLiteral)


def _string_literal_preeval(obj):
    if isinstance(obj.value, str):
        return obj.value
    return ''.join(obj.value)


StringLiteral.preevaluate = _string_literal_preeval

# Loops
UntilDo = create_model_element_type('UntilDo', ('name', 'until', 'do', 'otherwise'),
                                    specs=ElementSpecs(new_scope=True, isolate_scope=True))
""" """
ForEvery = create_model_element_type('ForEvery', ('name', 'item_name', 'iterable', 'do'),
                                     specs=ElementSpecs(new_scope=True, isolate_scope=True))
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
Modify = create_model_element_type('Modify', ('subject', 'modifiers'),
                                   specs=ElementSpecs(
                                       new_scope=True,
                                       isolate_scope=True,
                                   ))
""" """
ModifierCall = create_model_element_type('ModifierCall', ('modifier', 'args'),
                                         specs=ElementSpecs(always_use_scope=True))
""" """
ModifierDef = create_model_element_type('ModifierDef', ('target', 'parameters', 'definition'),
                                        specs=ElementSpecs(
                                            new_scope=True,
                                            isolate_scope=True,
                                            retain_scope=True,
                                        ))
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
Reduce = create_model_element_type('Reduce', specs=ElementSpecs(always_use_scope=True))
""" """

NewBag = create_model_element_type('NewBag', constant=True)
""" """

Reference = create_model_element_type('Reference')
""" """
Reference.register(SpecialReference)

ClearValue = create_model_element_type('ClearValue')
""" """

# Predicates
IfThen = create_model_element_type('IfThen', ('predicate', 'then', 'otherwise'),
                                   basic_predicated=True)
""" """
UseIf = create_model_element_type('UseIf', ('use', 'predicate', 'otherwise'),
                                  specs=ElementSpecs(
                                      predicate_info=('predicate', 'use', 'otherwise'),
                                  ))
""" """


class Dice(namedtuple('_DiceBase', ('number_of_dice', 'sides', 'codeinfo')), ModelElement):
    """
    """

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.codeinfo.text
