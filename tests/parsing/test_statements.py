# pylint: disable=missing-docstring,unused-import,no-member
from .util import create_scripttest_func

test_assignment = create_scripttest_func('assignment')
test_load = create_scripttest_func('load')
test_modifier_defs = create_scripttest_func('modifier_defs')
#FIXME
# test_flow_control = create_scripttest_func('flow_control')
