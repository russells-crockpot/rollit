# pylint: disable=missing-docstring
import pytest

from rollit.ast import ModelElement, ModelEnumElement
from rollit.objects import InternalObject

from .conftest import script_tests
from ..util import reorder_keys


def _convert_values(value):
    # if isinstance(value, ModelEnumElement):
    if isinstance(value, ModelElement) and not isinstance(value, ModelEnumElement):
        value = tuple(value[:-1])
    if isinstance(value, InternalObject):
        # pylint: disable=protected-access
        value = value._to_eval_test_repr()
    if isinstance(value, (list, set, tuple)):
        compact = set(value)
        if len(compact) == 1 and compact.pop() is None:
            return None
        return tuple(_convert_values(v) for v in value)
    if isinstance(value, dict):
        return {k: _convert_values(v) for k, v in value.items()}
    return value


def create_scripttest_func(category):

    def _func(runner, scripttest):
        with runner.use_source('testing'):
            for statement, expected in scripttest.statements:
                actual = runner.run(statement)
                actual = _convert_values(actual)
                if isinstance(actual, dict):
                    actual = reorder_keys(expected, actual)
                assert expected == actual

    _func.__name__ = f'test_{category}'
    return pytest.mark.parametrize('scripttest', getattr(script_tests, category))(_func)
