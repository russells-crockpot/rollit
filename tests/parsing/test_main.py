# pylint: disable=missing-docstring,unused-import,no-member

import pytest
from .conftest import script_tests
from .util import reorder_keys


@pytest.mark.parametrize('scripttest', script_tests.math)
def test_math(parser, scripttest):
    actual_result = parser.parse(scripttest.script)
    assert len(scripttest.result) == len(actual_result)
    assert scripttest.result == reorder_keys(scripttest.result, actual_result)


@pytest.mark.parametrize('scripttest', script_tests.dice)
def test_dice(parser, scripttest):
    actual_result = parser.parse(scripttest.script)
    assert len(scripttest.result) == len(actual_result)
    assert scripttest.result == reorder_keys(scripttest.result, actual_result)


@pytest.mark.parametrize('scripttest', script_tests.pack)
def test_pack(parser, scripttest):
    actual_result = parser.parse(scripttest.script)
    assert len(scripttest.result) == len(actual_result)
    assert scripttest.result == reorder_keys(scripttest.result, actual_result)


@pytest.mark.parametrize('scripttest', script_tests.modify)
def test_modify(parser, scripttest):
    actual_result = parser.parse(scripttest.script)
    assert len(scripttest.result) == len(actual_result)
    assert scripttest.result == reorder_keys(scripttest.result, actual_result)
