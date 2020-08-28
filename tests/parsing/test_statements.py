# pylint: disable=missing-docstring,unused-import,no-member
from .util import create_scripttest_func

test_assignment = create_scripttest_func('assignment')
test_load = create_scripttest_func('load')
test_blocks = create_scripttest_func('blocks')
test_attempt = create_scripttest_func('attempt')
