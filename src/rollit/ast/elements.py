"""
"""
from collections import namedtuple

from .base import create_model_element_type, ElementSpecs, ModelEnumElement, ModelElement

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


class RestartLocationSpecifier(ModelEnumElement):
    """
    """
    AT = 'at'
    BEFORE = 'before'
    AFTER = 'after'


StringLiteral = create_model_element_type('StringLiteral', specs=ElementSpecs(intern_strings=False))
""" """


def _string_literal_preeval(obj):
    if isinstance(obj.value, str):
        return obj.value
    return ''.join(obj.value)


StringLiteral.preevaluate = _string_literal_preeval

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

NewBag = create_model_element_type('NewBag', constant=True)
""" """

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

    def __str__(self):
        numdice = self.number_of_dice
        if isinstance(numdice, str):
            numdice = f'{{{numdice}}}'
        sides = self.sides
        if isinstance(sides, str):
            sides = f'{{{sides}}}'
        return f'{numdice}d{sides}'
