# pylint: disable=missing-docstring
from lacewing.install import basic as _
import copy
import itertools
import pathlib
from collections import namedtuple

import pytest
import tatsu

from rollit.semantics import RollItSemantics

try:
    from ruamel import yaml
except ImportError:
    import yaml

__DEFAULT_GRAMMAR_FILE = pathlib.Path(__file__).parent.parent.parent / 'grammar.tatsu'


def __load():
    _script_tests_by_category = {}

    class _ScriptTest(namedtuple('_ScriptTestBase', ('script', 'result'))):

        def __new__(cls, entry, parent_categories=(), *, _copying=False):
            if _copying:
                return super().__new__(cls, **entry)
            categories = tuple(itertools.chain(entry.get('categories', ()), parent_categories))
            tests = tuple(cls(child, categories) for child in entry.get('tests', ()))
            script = entry.get('script')
            result = entry.get('result')
            self = super().__new__(
                cls,
                script=script,
                result=result,
            )
            # We only want to add tests that are actual tests.
            if self.script and self.result:
                for category in categories:
                    _script_tests_by_category.setdefault(category, []).append(self)
                return self
            return None

        def copy(self):
            d = self._asdict()
            if isinstance(self.result, (dict, tuple, set, list)):
                d['result'] = copy.deepcopy(self.result)
            return type(self)(d, _copying=True)

        def __str__(self):
            return f'<{type(self).__name__[1:]}: {self.script}>'

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

try:
    del __load
except Exception:
    pass


@pytest.fixture(scope='session')
def parser(request):
    with open(request.config.getoption('grammar_file')) as f:
        grammar = f.read()
    return tatsu.compile(grammar, semantics=RollItSemantics())


def pytest_addoption(parser):
    parser.addoption(
        '--grammar-file',
        default=str(__DEFAULT_GRAMMAR_FILE),
        help='The grammar file to use.',
    )
