# pylint: disable=missing-docstring
import itertools

import pytest
from rollit.ast import ModelElement

from .conftest import script_tests
from ..util import reorder_keys


def create_scripttest_func(category):

    def _func(parser, scripttest):
        expected_results = scripttest.result
        if not isinstance(expected_results, (tuple, list, set)):
            expected_results = (expected_results,)
        actual_results = parser(scripttest.script)
        if isinstance(actual_results, ModelElement):
            # pylint: disable=protected-access
            actual_results = (actual_results._to_test_dict(),)
        if not isinstance(actual_results, (tuple, list, set)):
            actual_results = (actual_results,)
        for expected, actual in itertools.zip_longest(expected_results, actual_results):
            if isinstance(actual, ModelElement):
                # pylint: disable=protected-access
                actual = actual._to_test_dict()
            actual = reorder_keys(expected, actual)
            if isinstance(expected, (list, set)):
                expected = tuple(expected)
            assert expected == actual

    _func.__name__ = f'test_{category}'
    return pytest.mark.parametrize('scripttest', getattr(script_tests, category))(_func)
