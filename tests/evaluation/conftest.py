# pylint: disable=missing-docstring
import copy
import itertools
import functools
import pathlib
from collections import namedtuple
from contextlib import suppress

import pytest

from rollit.runtime import Runner
from rollit.runtime.towers import IncrementalTower
from rollit.ast import actions, is_valid_iterable

try:
    from ruamel import yaml
except ImportError:
    import yaml


def __load():
    ScriptStatement = namedtuple('Stmt', ('statement', 'result'))
    _script_tests_by_category = {}

    def _convert_lists(entry):
        if isinstance(entry, dict):
            return {k: _convert_lists(v) for k, v in entry.items()}
        elif isinstance(entry, list):
            return tuple(_convert_lists(i) for i in entry)
        return entry

    class _ScriptTest(namedtuple('_ScriptTestBase', ('statements',))):

        def __new__(cls, entry, parent_categories=(), *, _copying=False):
            if _copying:
                return super().__new__(cls, **entry)
            categories = tuple(itertools.chain(entry.get('categories', ()), parent_categories))
            tests = tuple(cls(child, categories) for child in entry.get('tests', ()))
            script = entry.get('script')
            statements = []
            for s, r in entry.get('statements', ()):
                statements.append(ScriptStatement(s, _convert_lists(r)))
            self = super().__new__(
                cls,
                statements=tuple(statements),
            )
            # We only want to add tests that are actual tests.
            if self.statements:
                for category in categories:
                    _script_tests_by_category.setdefault(category, []).append(self)
                return self
            return None

        def __str__(self):
            return f'ST({" | ".join(s.statement for s in self.statements)})'

        def __repr__(self):
            return str(self)

        def __eq__(self, actual):
            pass

    for path in (pathlib.Path(__file__).parent / 'scripts').iterdir():
        with path.open() as f:
            _ScriptTest(yaml.safe_load(f))
    for cat, items in _script_tests_by_category.items():
        _script_tests_by_category[cat] = tuple(items)
    ScriptTests = namedtuple('ScriptTests', tuple(_script_tests_by_category.keys()))
    return ScriptTests(**_script_tests_by_category)


script_tests = __load()

with suppress(Exception):
    del __load


@pytest.fixture
def runner():
    return Runner(dice_tower=IncrementalTower())
