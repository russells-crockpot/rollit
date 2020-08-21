# pylint: disable=missing-docstring, no-member
"""
"""
import enum
from abc import ABCMeta
from collections import namedtuple

ModelElement = ABCMeta('ModelElement', (tuple,), {})


class SingletonElement(tuple):
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


ModelElement.register(SingletonElement)


class FlowControlConstant(enum.Enum):
    SKIP = 'skip'
    STOP = 'stop'


ModelElement.register(FlowControlConstant)


class Reference(SingletonElement, metaclass=ABCMeta):

    def __new__(cls, value):
        if value == '?':
            return SpecialReference.MODIFYING
        if value == '~':
            return SpecialReference.ROOT
        if value == '*':
            return SpecialReference.ALL
        if value == '!':
            return SpecialReference.NONE
        return super().__new__(cls, value)


class SpecialReference(enum.Enum):
    MODIFYING = '?'
    ROOT = '~'
    ALL = '*'
    NONE = '!'


Reference.register(SpecialReference)
ModelElement.register(SpecialReference)

Assignment = namedtuple('Assignment', ('target', 'value'))
Load = namedtuple('Load', ('to_load', 'from_dialect', 'into'))
ModifierCall = namedtuple('ModifierCall', ('modifier', 'args'))
Modify = namedtuple('Modify', ('modifying', 'modifiers'))
Access = namedtuple('Access', ('accessing', 'accessors'))
Enlarge = namedtuple('Enlarge', ('size', 'value'))
Comparison = namedtuple('Comparison', ('left', 'op', 'right'))
If = namedtuple('If', ('predicate', 'then', 'otherwise'))
UseIf = namedtuple('UseIf', ('use', 'predicate', 'otherwise'))
ModifierDef = namedtuple('ModifierDef', ('target', 'parameters', 'definition'))
Dice = namedtuple('Dice', ('number_of_dice', 'sides'))
RollMath = namedtuple('RollMath', ('left', 'op', 'right'))
Math = namedtuple('Math', ('left', 'op', 'right'))
UntilDo = namedtuple('UntilDo', ('until', 'do', 'otherwise'))
Negation = type('Negation', (SingletonElement,), {})
FullStop = type('FullStop', (SingletonElement,), {})
Reduce = type('Reduce', (SingletonElement,), {})
Length = type('Length', (SingletonElement,), {})

ModelElement.register(Assignment)
ModelElement.register(Load)
ModelElement.register(ModifierCall)
ModelElement.register(Modify)
ModelElement.register(Access)
ModelElement.register(Enlarge)
ModelElement.register(Comparison)
ModelElement.register(If)
ModelElement.register(UseIf)
ModelElement.register(ModifierDef)
ModelElement.register(Dice)
ModelElement.register(RollMath)
ModelElement.register(Math)
ModelElement.register(UntilDo)
