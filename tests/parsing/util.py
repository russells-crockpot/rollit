# pylint: disable=missing-docstring
import itertools
from importlib import import_module

import pytest
from rollit.model import ModelElement

from .conftest import script_tests

_MONKEYPATCH_VALUES = ()

_VALUES_MAP = {
    '_operator': {
        'mul': '*',
        'add': '+',
        'sub': '-',
        'truediv': '/',
        'floordiv': '//',
        'mod': '%',
    }
}


def create_scripttest_func(category):

    def _func(parser, monkeypatch, scripttest):
        for module_name, overrides in _MONKEYPATCH_VALUES:
            module = import_module(module_name)
            for attr, v in overrides:
                monkeypatch.setattr(module, attr, v)
        expected_results = scripttest.result
        if not isinstance(expected_results, (tuple, list, set)):
            expected_results = (expected_results,)
        actual_results = tuple(
            ast_element_to_dict(stmt)
            for stmt in parser.parse(scripttest.script)
            if not isinstance(stmt, str))
        for expected, actual in itertools.zip_longest(expected_results, actual_results):
            assert expected == reorder_keys(expected, actual)

    _func.__name__ = f'test_{category}'
    return pytest.mark.parametrize('scripttest', getattr(script_tests, category))(_func)


def ast_element_to_dict(elem):
    if not isinstance(elem, ModelElement):
        if isinstance(elem, (tuple, list, set)):
            return type(elem)(ast_element_to_dict(e) for e in elem)
        if hasattr(elem, '__module__'):
            if elem.__module__ in _VALUES_MAP and elem.__name__ in _VALUES_MAP[elem.__module__]:
                return _VALUES_MAP[elem.__module__][elem.__name__]
        return elem
    rval = {'_class': type(elem).__name__}
    for k, v in zip(elem._fields, elem):
        rval[k] = ast_element_to_dict(v)
    return rval


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
