# pylint: disable=missing-docstring, no-member
"""
"""
import enum
from abc import ABCMeta
from collections import namedtuple

ModelElement = ABCMeta('ModelElement', (tuple,), {})


class SingleValueElement(ModelElement):
    """
    """

    def __new__(cls, value):
        if isinstance(value, ModelElement) or not isinstance(value, (tuple, list, set)):
            value = (value,)
        return super().__new__(cls, value)

    @property
    def value(self):
        """
        """
        return self[0]

    def __str__(self):
        return f'<{type(self).__name__}: {self.value}>'

    def __repr__(self):
        return f'{type(self).__name__}({self.value!r})'


class SequenceValueElement(ModelElement):
    """
    """

    def __str__(self):
        return f'<{type(self).__name__}: {super().__str__()}>'

    def __repr__(self):
        return f'{type(self).__name__}{super().__repr__()}'


class SpecialReference(enum.Enum):
    SUBJECT = '?'
    ROOT = '~'
    ALL = '*'
    NONE = '!'
    LOCAL = '$'


ModelElement.register(SpecialReference)


class RestartLocationSpecifier(enum.Enum):
    AT = 'at'
    BEFORE = 'before'
    AFTER = 'after'


class SingleWordStatment(enum.Enum):
    LEAVE = 'leave'


ModelElement.register(SingleWordStatment)


def create_model_element_type(name, attrs=()):
    """
    """
    if not attrs:
        bases = (SingleValueElement,)
    else:
        bases = (namedtuple(f'_{name}Base', attrs), ModelElement)
    return type(name, bases, {})


# Loops
UntilDo = create_model_element_type('UntilDo', ('name', 'until', 'do', 'otherwise'))
ForEvery = create_model_element_type('ForEvery', ('name', 'item_name', 'iterable', 'do'))
# Flow Control
Restart = create_model_element_type('Restart', ('location_specifier', 'target'))
# pylint: disable=protected-access
for spec in RestartLocationSpecifier:
    # pylint: disable=too-many-function-args
    setattr(Restart, f'{spec._name_}_ROOT', Restart(spec, SpecialReference.ROOT))
    # pylint: disable=too-many-function-args
    setattr(Restart, f'{spec._name_}_NONE', Restart(spec, SpecialReference.NONE))
# pylint: disable=undefined-loop-variable
del spec

Assignment = create_model_element_type('Assignment', ('target', 'value'))
Load = create_model_element_type('Load', ('to_load', 'load_from', 'into'))
ModifierCall = create_model_element_type('ModifierCall', ('modifier', 'args'))
Modify = create_model_element_type('Modify', ('subject', 'modifiers'))
Access = create_model_element_type('Access', ('accessing', 'accessors'))
Enlarge = create_model_element_type('Enlarge', ('size', 'value'))
Dice = create_model_element_type('Dice', ('number_of_dice', 'sides'))
BinaryOp = create_model_element_type('BinaryOp', ('left', 'op', 'right'))
Negation = create_model_element_type('Negation')
Reduce = create_model_element_type('Reduce')
Length = create_model_element_type('Length')
CreateBag = create_model_element_type('CreateBag')
StringLiteral = create_model_element_type('StringLiteral')
If = create_model_element_type('If', ('predicate', 'then', 'otherwise'))
UseIf = create_model_element_type('UseIf', ('use', 'predicate', 'otherwise'))
ModifierDef = create_model_element_type('ModifierDef', ('target', 'parameters', 'definition'))
