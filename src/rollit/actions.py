# pylint: disable=missing-function-docstring
"""
"""
import inspect
import functools
from collections import namedtuple
from collections.abc import Mapping
from contextlib import suppress

from . import model
from .grammar import TreeNode

__all__ = ['Actions']

_STATEMENT_ENDS = frozenset(('\n', '\r', '|', ''))

#FIXME Unicode escapes
_ESCAPE_MAP = {
    r'\n': '\n',
    r'\r': '\r',
    r'\f': '\f',
    r"\'": "'",
    r'\v': '\v',
    r'\b': '\b',
}


def _unwrap_node(node):
    if isinstance(node, (list, tuple)) and not isinstance(node, model.ModelElement):
        items = type(node)(nd for nd in (_unwrap_node(n) for n in node) if nd)
        with suppress(TypeError):
            if len(items) == 1:
                return items[0]
        return items
    if not isinstance(node, TreeNode):
        return node
    elements = _unwrap_node(node.elements)
    with suppress(TypeError):
        if len(elements) == 1:
            return elements[0]
    return elements


# pylint: disable=too-complex
def elements_to_values(*, text_only=False, elements_only=False, must_have_text=False, unwrap=True):
    """
    """

    def _decorator(func):

        @functools.wraps(func)
        def _wrapper(*args):
            values = []
            for element in args[-1]:
                if not element:
                    continue
                if isinstance(element, TreeNode):
                    if must_have_text and not element.text.strip():
                        continue
                    if elements_only:
                        element = element.elements
                    elif text_only:
                        element = element.text.strip()
                    else:
                        element = element.elements or element.text.strip()
                if element:
                    if unwrap:
                        element = _unwrap_node(element)
                    values.append(element)
            return func(*args[:-1], values)

        return _wrapper

    return _decorator


class CreateTypeProperty(
        namedtuple('_CreateTypePropertyBase',
                   ('model_cls', 'single_value', 'defaults', 'value_indexes'))):
    """
    """

    def __new__(cls, model_cls, value_indexes=None, single_value=None, defaults=None):
        if single_value is None:
            single_value = True
            if inspect.isclass(model_cls) \
                    and issubclass(model_cls, (model.ModelElement, Mapping)) \
                    and not issubclass(model_cls, model.SingleValueElement):
                single_value = False
        if single_value and defaults:
            defaults = model_cls(defaults)
        if isinstance(value_indexes, dict):
            value_indexes = tuple(value_indexes.items())
        return super().__new__(
            cls,
            model_cls=model_cls,
            single_value=single_value,
            defaults=defaults,
            value_indexes=value_indexes,
        )

    @elements_to_values()
    def __call__(self, text, start, end, values):
        if self.single_value:
            if not values:
                return self.defaults
            if self.value_indexes is not None:
                return self.model_cls(values[self.value_indexes])
            return self.model_cls(values[0])
        if self.value_indexes:
            # TODO add defaults
            mapped_values = {name: values[idx] for name, idx in self.value_indexes}
            return self.model_cls(**mapped_values)
        return self.model_cls(*values)


# pylint: disable=unexpected-keyword-arg,no-value-for-parameter
class Actions:
    """
    """
    binary_op = CreateTypeProperty(model.BinaryOp)
    use_if = CreateTypeProperty(model.UseIf, (('use', 1), ('predicate', 3), ('otherwise', 5)))
    length = CreateTypeProperty(model.Length, -1, single_value=True)
    dice = CreateTypeProperty(model.Dice, (('number_of_dice', 0), ('sides', -1)))

    @elements_to_values(text_only=True)
    def int(self, text, start, end, values):
        return int(''.join(values))

    @elements_to_values(text_only=True)
    def float(self, text, start, end, values):
        return float(''.join(values))

    def special_ref(self, text, start, end, values):
        return model.SpecialReference(text[start:end])

    def text(self, text, start, end, values):
        return text[start:end]

    @elements_to_values()
    def accessor(self, text, start, end, values):
        return values[-1]

    def ignore(self, *args):
        return None

    def _negate(self, element):
        if isinstance(element, model.Negation):
            return element.value
        return model.Negation(element)

    @elements_to_values()
    def parens(self, text, start, end, values):
        return values[1]

    @elements_to_values()
    def negate(self, text, start, end, values):
        return self._negate(values[-1])

    @staticmethod
    def _to_tuple(item):
        if isinstance(item, model.ModelElement) or not isinstance(item, (list, tuple)):
            return (item,)
        if isinstance(item, list):
            return tuple(item)
        return item

    @elements_to_values()
    def modify(self, text, start, end, values):
        return model.Modify(subject=values[0], modifiers=self._to_tuple(values[-1]))

    @elements_to_values()
    def access(self, text, start, end, values):
        return model.Access(accessing=values[0], accessors=self._to_tuple(values[-1]))

    @elements_to_values()
    def modifier_call(self, text, start, end, values):
        if len(values) == 1:
            return model.ModifierCall(modifier=values[0], args=())
        return model.ModifierCall(modifier=values[0], args=self._to_tuple(values[-1]))

    @elements_to_values()
    def reduce(self, text, start, end, values):
        value = values[1]
        if isinstance(value, model.Enlarge):
            return value
        if value == '*':
            value = model.SpecialReference.ALL
        return model.Reduce(value)

    @elements_to_values()
    def enlarge(self, text, start, end, values):
        size = value = None
        sep_idx = values.index('@')
        with suppress(IndexError):
            size = values[:sep_idx][0]
        with suppress(IndexError):
            value = values[sep_idx + 1:][0]
        return model.Enlarge(size=size, value=value)

    @elements_to_values()
    def modifier_args(self, text, start, end, values):
        if len(values) == 2:
            return ()
        return tuple(values[1:-1])
