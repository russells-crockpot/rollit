"""
"""
import enum
import sys
from abc import ABCMeta
from collections import namedtuple

__all__ = [
    'DeferEvaluation',
    'ElementSpecs',
    'CodeInfo',
    'ModelElement',
    'ModelEnumElement',
    'SingleValueElement',
    'SequenceValueElement',
    'ConstantElement',
    'create_model_element_type',
]


def __create_defer_evaluation():

    class _DeferEvaluationBase(tuple):
        __the_object = None

        def __new__(cls):
            if not cls.__the_object:
                cls.__the_object = super().__new__(cls)
            return cls.__the_object

        def __bool__(self):
            return False

        @staticmethod
        def __str__():
            return 'DeferEvaluation'

    return _DeferEvaluationBase()


DeferEvaluation = __create_defer_evaluation()
""" """
del __create_defer_evaluation

ElementSpecs = namedtuple('ElementSpecs', ('predicate_info', 'intern_strings', 'new_scope',
                                           'isolate_scope', 'retain_scope', 'always_use_scope'),
                          defaults=((), True, False, False, False, False))
""" """

CodeInfo = namedtuple('CodeInfo', ('text', 'start_pos', 'end_pos'))
""" """


class ModelElementMeta(ABCMeta):
    """
    """
    _evaluator = _reducer = None

    def evaluator(cls, func):
        """
        """
        cls._evaluator = func
        return func

    def reducer(cls, func):
        """
        """
        cls._reducer = func
        return func


class ModelElement(namedtuple('_ModelElementBase', ('codeinfo',)), metaclass=ModelElementMeta):
    """
    """
    __specs__ = ElementSpecs()

    def __new__(cls, *args, codeinfo, **kwargs):
        if isinstance(codeinfo, dict):
            codeinfo = CodeInfo(**codeinfo)
        elif not isinstance(codeinfo, CodeInfo) and codeinfo is not None:
            codeinfo = CodeInfo(*codeinfo)
        if cls.__specs__.intern_strings:
            args = (sys.intern(a) if isinstance(a, str) else a for a in args)
            for k, v in kwargs.items():
                if isinstance(v, str):
                    kwargs[k] = v
        return super().__new__(cls, *args, codeinfo=codeinfo, **kwargs)

    @classmethod
    def preevaluate(cls, value):
        """
        """
        return DeferEvaluation

    def reduce(self, context):
        """
        """
        # pylint: disable=no-member
        return self._reducer(context)

    def evaluate(self, context):
        """
        """
        # pylint: disable=no-member
        return self._evaluator(context)

    @staticmethod
    # pylint: disable=protected-access
    def _get_test_value(item):
        if isinstance(item, enum.Enum):
            return {
                '_class': type(item).__name__,
                'value': item._name_,
            }
        if isinstance(item, ModelElement):
            return item._to_test_dict()
        if isinstance(item, (tuple, list, set)):
            return tuple(ModelElement._get_test_value(i) for i in item)
        return item

    def _to_test_dict(self):
        """
        """
        rval = self._asdict()
        rval.pop('codeinfo', None)
        for k, v in rval.items():
            rval[k] = self._get_test_value(v)
        rval['_class'] = type(self).__name__
        return rval


class ModelEnumElement(enum.Enum):
    """
    """

    # pylint: disable=missing-function-docstring
    def _to_test_dict(self):
        # pylint: disable=no-member
        return {'_class': type(self).__name__, 'value': self._name_}

    @classmethod
    def preevaluate(cls, value):
        return DeferEvaluation


ModelElement.register(ModelEnumElement)
ModelEnumElement.__specs__ = ElementSpecs()


class _PredicatedElementMixIn:
    """
    """

    @staticmethod
    def _evaluate_predicate(predicate):
        if isinstance(predicate, (int, float)):
            return bool(predicate)
        if not predicate:
            return False
        if isinstance(predicate, ModelElement):
            return predicate.preevaluate(predicate)
        return DeferEvaluation

    def __new__(cls, *args, _suppress_evaluation=False, **kwargs):
        self = super().__new__(cls, *args, **kwargs)
        if _suppress_evaluation:
            return self
        resp = cls._evaluate_predicate(getattr(self, cls.__specs__.predicate_info[0]))
        if resp is DeferEvaluation:
            return self
        if resp:
            return getattr(self, cls.__specs__.predicate_info[1])
        if len(cls.__specs__.predicate_info) >= 3:
            return getattr(self, cls.__specs__.predicate_info[2])
        return None


class SingleValueElement(namedtuple('_SingleValueElementBase', ('value', 'codeinfo')),
                         ModelElement):
    """
    """

    def __new__(cls, value, *, codeinfo):
        return super().__new__(cls, value, codeinfo=codeinfo)

    def __str__(self):
        return f'<{type(self).__name__}: {self.value}>'

    def __repr__(self):
        return f'{type(self).__name__}({self.value!r}, codeinfo={self.codeinfo!r})'

    def _to_test_dict(self):
        return {'_class': type(self).__name__, 'value': self.value}

    def _to_test_dict(self):
        return {
            '_class': type(self).__name__,
            'value': ModelElement._get_test_value(self.value),
        }


#FIXME Deal with codeinfo and it's value
class SequenceValueElement(ModelElement):
    """
    """

    def __str__(self):
        return f'<{type(self).__name__}: {super().__str__()}>'

    def __repr__(self):
        return f'{type(self).__name__}{super().__repr__()}'

    def _to_test_dict(self):
        return {
            '_class': type(self).__name__,
            'items': tuple(ModelElement._get_test_value(item) for item in self),
        }


class ConstantElement(ModelElement):
    """
    """

    def __new__(cls, *, codeinfo):
        return super().__new__(cls, codeinfo=codeinfo)

    def __str__(self):
        return type(self).__name__

    def __repr__(self):
        return f'{self}()'

    def __bool__(self):
        return True

    @classmethod
    def _to_test_dict(cls):
        return {'_class': cls.__name__}


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
            bases = (_PredicatedElementMixIn, namedtuple(f'_{name}Base', attrs), ModelElement)
        else:
            bases = (namedtuple(f'_{name}Base', attrs), ModelElement)
    class_attrs.setdefault('__specs__', specs)
    return type(name, bases, class_attrs)
