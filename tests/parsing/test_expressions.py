# pylint: disable=missing-docstring,unused-import,no-member
from importlib import import_module

import pytest

from .conftest import script_tests
from .util import reorder_keys, ast_element_to_dict

_MONKEYPATCH_VALUES = ()


def _create_test_func(category):

    def _func(parser, monkeypatch, scripttest):
        for module_name, overrides in _MONKEYPATCH_VALUES:
            module = import_module(module_name)
            for attr, v in overrides:
                monkeypatch.setattr(module, attr, v)
        actual_result = ast_element_to_dict(parser.parse(scripttest.script)[0])
        assert scripttest.result == reorder_keys(scripttest.result, actual_result)

    _func.__name__ = f'test_{category}'
    return pytest.mark.parametrize('scripttest', getattr(script_tests, category))(_func)


test_atoms = _create_test_func('atoms')
test_math = _create_test_func('math')
test_dice = _create_test_func('dice')
test_modify = _create_test_func('modify')
test_blocks = _create_test_func('blocks')
test_rolls = _create_test_func('rolls')
# test_freeze = _create_test_func('freeze')
# test_length = _create_test_func('length')
