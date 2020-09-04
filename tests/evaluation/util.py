# pylint: disable=missing-docstring
import pytest

from rollit.ast import ModelElement
from rollit.execution.objects import Dice, Bag

from .conftest import script_tests
from ..util import reorder_keys


def _convert_values(value):
    if isinstance(value, ModelElement):
        value = tuple(value[:-1])
    if isinstance(value, Dice):
        return (value.num_dice, value.sides)
    if isinstance(value, (list, set, tuple)):
        return tuple(_convert_values(v) for v in value)
    if isinstance(value, Bag):
        # pylint: disable=protected-access
        value = value._entries
    if isinstance(value, dict):
        return {k: _convert_values(v) for k, v in value.items()}
    return value


def create_scripttest_func(category):

    def _func(runner, scripttest):
        for statement, expected in scripttest.statements:
            actual = runner.run(statement)
            actual = _convert_values(actual)
            if isinstance(actual, dict):
                actual = reorder_keys(expected, actual)
            assert expected == actual

    _func.__name__ = f'test_{category}'
    return pytest.mark.parametrize('scripttest', getattr(script_tests, category))(_func)
