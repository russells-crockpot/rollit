# pylint: disable=missing-docstring, no-member
"""
"""
import enum
import operator
from abc import ABCMeta
from collections import namedtuple, OrderedDict


def _raise_not_implemented(*args):
    raise NotImplementedError


KEYWORDS = frozenset({
    'after',
    'always',
    'at',
    'attempt',
    'before',
    'but',
    'Clear',
    'do',
    'every',
    'except',
    'for',
    'from',
    'has',
    'if',
    'into',
    'isa',
    'leave',
    'load',
    'not',
    'occurs',
    'oops',
    'otherwise',
    'restart',
    'that',
    'then',
    'unless',
    'until',
    'use',
    'when',
})

OPERATOR_MAP = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
    '%/': operator.truediv,
    '%': operator.mod,
    '>': operator.gt,
    '<': operator.lt,
    '==': operator.eq,
    '!=': operator.ne,
    '>=': operator.ge,
    '<=': operator.le,
    'has': lambda x, y: y in x,
    'and': operator.and_,
    'or': operator.or_,
    'isa': _raise_not_implemented,
    '&': _raise_not_implemented,
    '^': _raise_not_implemented,
}

MATH_OPERATORS = frozenset({'+', '-', '*', '/', '%/', '%'})

DEFER_EVALUATION = object()


#TODO
class _ObjectCache(OrderedDict):
    pass


def evaluate_predicate(predicate):
    if isinstance(predicate, StringLiteral):
        return bool(predicate.value)
    if isinstance(predicate, (int, float)):
        return bool(predicate)
    if predicate == SpecialReference.NONE:
        return False
    return DEFER_EVALUATION


ModelElement = ABCMeta('ModelElement', (tuple,), {})


class _PredicatedElementMixIn:
    """
    """
    _predicate_info = ()

    def __new__(cls, *args, _suppress_evaluation=False, **kwargs):
        self = super().__new__(cls, *args, **kwargs)
        if _suppress_evaluation:
            return self
        resp = evaluate_predicate(getattr(self, cls._predicate_info[0]))
        if resp == DEFER_EVALUATION:
            return self
        if resp:
            return getattr(self, cls._predicate_info[1])
        if len(cls._predicate_info) >= 3:
            return getattr(self, cls._predicate_info[2])
        return None


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


class SpecialAccessor(enum.Enum):
    LENGTH = '#'
    TOTAL = '+'
    VALUE = '='
    EVERY = '*'


ModelElement.register(SpecialAccessor)


class SpecialReference(enum.Enum):
    SUBJECT = '?'
    ROOT = '~'
    ALL = '*'
    NONE = '!'
    LOCAL = '$'
    ERROR = '#'


ModelElement.register(SpecialReference)


class RestartLocationSpecifier(enum.Enum):
    AT = 'at'
    BEFORE = 'before'
    AFTER = 'after'


class ConstantElement(ModelElement):
    """
    """

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._THE_OBJECT = None

    def __new__(cls):
        if cls._THE_OBJECT is None:
            cls._THE_OBJECT = super().__new__(cls)
        return cls._THE_OBJECT

    def __str__(self):
        return type(self).__name__

    def __repr__(self):
        return f'{self}()'

    def __bool__(self):
        return True


def create_model_element_type(name,
                              attrs=(),
                              predicated=False,
                              constant=False,
                              *,
                              predicate_info=()):
    """
    """
    class_attrs = {}
    if predicated and not predicate_info:
        predicate_info = tuple(attrs[:3])
    if constant:
        bases = (ConstantElement,)
    elif not attrs:
        bases = (SingleValueElement,)
    elif predicate_info:
        bases = (_PredicatedElementMixIn, namedtuple(f'_{name}Base', attrs), ModelElement)
        class_attrs = {'_predicate_info': predicate_info}
    else:
        bases = (namedtuple(f'_{name}Base', attrs), ModelElement)
    return type(name, bases, class_attrs)


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

# Error Handling
Attempt = create_model_element_type('Attempt', ('attempt', 'buts', 'always'))
ButIf = create_model_element_type('ButIf', ('predicate', 'statement'), True)
Oops = create_model_element_type('Oops')

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
ClearValue = create_model_element_type('ClearValue')
StringLiteral = create_model_element_type('StringLiteral')
IfThen = create_model_element_type('IfThen', ('predicate', 'then', 'otherwise'), True)
UseIf = create_model_element_type('UseIf', ('use', 'predicate', 'otherwise'),
                                  predicate_info=('predicate', 'use', 'otherwise'))
ModifierDef = create_model_element_type('ModifierDef', ('target', 'parameters', 'definition'))
Leave = create_model_element_type('Leave', constant=True)
NewBag = create_model_element_type('NewBag', constant=True)
