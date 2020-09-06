# pylint: disable=missing-docstring,unused-import,no-member
from .util import create_scripttest_func

test_empty_bags = create_scripttest_func('empty_bags')
test_bag_access = create_scripttest_func('bag_access')
test_bag_definitions = create_scripttest_func('bag_definitions')
test_special_entries = create_scripttest_func('special_entries')
test_bag_parents = create_scripttest_func('bag_parents')
