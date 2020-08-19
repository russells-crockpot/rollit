# pylint: disable=missing-docstring
import itertools


def reorder_keys(d1, d2):
    if not isinstance(d2, dict):
        #pylint: disable=unidiomatic-typecheck
        assert type(d1) == type(d2)
        return d2
    newd = {}
    for k, v1 in d1.items():
        v2 = d2[k]
        if isinstance(v1, dict):
            v2 = reorder_keys(v1, v2)
        elif isinstance(v1, (list, set, tuple)):
            v2 = type(v1)(reorder_keys(*z) for z in itertools.zip_longest(v1, v1))
        newd[k] = v2
    return newd
