# pylint: disable=missing-docstring, no-member
"""
"""
import enum
from abc import ABCMeta
from collections import namedtuple

ModelElement = ABCMeta('ModelElement', (tuple,), {})


class SingleValueElement(tuple):
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


ModelElement.register(SingleValueElement)


class Reference(SingleValueElement, metaclass=ABCMeta):

    def __new__(cls, value):
        if value == '?':
            return SpecialReference.SUBJECT
        if value == '~':
            return SpecialReference.ROOT
        if value == '*':
            return SpecialReference.ALL
        if value == '!':
            return SpecialReference.NONE
        return super().__new__(cls, value)


class SpecialReference(enum.Enum):
    SUBJECT = '?'
    ROOT = '~'
    ALL = '*'
    NONE = '!'


Reference.register(SpecialReference)
ModelElement.register(SpecialReference)


class RestartLocationSpecifier(enum.Enum):
    AT = 'at'
    BEFORE = 'before'
    AFTER = 'after'


# Loops
UntilDo = namedtuple('UntilDo', ('name', 'until', 'do', 'otherwise'))
ModelElement.register(UntilDo)
ForEvery = namedtuple('ForEvery', ('name', 'item_name', 'iterable', 'do'))
ModelElement.register(ForEvery)
# Flow Control
Restart = namedtuple('Restart', ('location_specifier', 'target'))
# pylint: disable=protected-access
for spec in RestartLocationSpecifier:
    setattr(Restart, f'{spec._name_}_ROOT', Restart(spec, SpecialReference.ROOT))
    setattr(Restart, f'{spec._name_}_NONE', Restart(spec, SpecialReference.NONE))
# pylint: disable=undefined-loop-variable
del spec
ModelElement.register(Restart)

Assignment = namedtuple('Assignment', ('target', 'value'))
Load = namedtuple('Load', ('to_load', 'from_dialect', 'into'))
ModifierCall = namedtuple('ModifierCall', ('modifier', 'args'))
Modify = namedtuple('Modify', ('subject', 'modifiers'))
Access = namedtuple('Access', ('accessing', 'accessors'))
Enlarge = namedtuple('Enlarge', ('size', 'value'))
Comparison = namedtuple('Comparison', ('left', 'op', 'right'))
If = namedtuple('If', ('predicate', 'then', 'otherwise'))
UseIf = namedtuple('UseIf', ('use', 'predicate', 'otherwise'))
ModifierDef = namedtuple('ModifierDef', ('target', 'parameters', 'definition'))
Dice = namedtuple('Dice', ('number_of_dice', 'sides'))
RollMath = namedtuple('RollMath', ('left', 'op', 'right'))
Math = namedtuple('Math', ('left', 'op', 'right'))
Negation = type('Negation', (SingleValueElement,), {})
Reduce = type('Reduce', (SingleValueElement,), {})
Length = type('Length', (SingleValueElement,), {})

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
