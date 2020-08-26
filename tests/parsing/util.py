# pylint: disable=missing-docstring
import enum
import itertools

import pytest
from rollit import model

from .conftest import script_tests


def get_element_value(elem):
    if not isinstance(elem, model.ModelElement) and not isinstance(elem, enum.Enum):
        if isinstance(elem, (tuple, list, set)):
            return type(elem)(get_element_value(item) for item in elem)
        return elem
    if isinstance(elem, enum.Enum):
        # pylint: disable=protected-access
        rval = {'value': elem._name_}
    elif isinstance(elem, model.SingleValueElement):
        rval = {'value': elem.value}
    else:
        rval = elem._asdict()
    for k, v in rval.items():
        rval[k] = get_element_value(v)
    rval['_class'] = type(elem).__name__
    return rval


def create_scripttest_func(category):

    def _func(parser, scripttest):
        expected_results = scripttest.result
        if not isinstance(expected_results, (tuple, list, set)):
            expected_results = (expected_results,)
        actual_results = get_element_value(parser(scripttest.script))
        if not isinstance(actual_results, (tuple, list, set)) \
                or isinstance(actual_results, model.ModelElement):
            actual_results = (actual_results,)
        for expected, actual in itertools.zip_longest(expected_results, actual_results):
            actual = reorder_keys(expected, actual)
            assert expected == actual

    _func.__name__ = f'test_{category}'
    return pytest.mark.parametrize('scripttest', getattr(script_tests, category))(_func)


def reorder_keys(expected, actual):
    if not isinstance(actual, dict):
        return actual
    result = {}
    for k, expected_value in expected.items():
        actual_value = actual[k]
        if isinstance(expected_value, dict):
            actual_value = reorder_keys(expected_value, actual_value)
        elif isinstance(expected_value, (list, set, tuple)):
            assert len(expected_value) == len(actual_value)
            actual_value = type(expected_value)(
                reorder_keys(*z) for z in itertools.zip_longest(expected_value, actual_value))
        result[k] = actual_value
    return result
