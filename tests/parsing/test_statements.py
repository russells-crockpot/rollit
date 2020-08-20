# pylint: disable=missing-docstring,unused-import,no-member
from .util import create_scripttest_func

test_load = create_scripttest_func('load')
test_load_from = create_scripttest_func('load_from')
test_modifier_defs = create_scripttest_func('modifier_defs')
test_assignment = create_scripttest_func('assignment')
#FIXME
# test_flow_control = create_scripttest_func('flow_control')
# test_blocks = create_scripttest_func('blocks')
