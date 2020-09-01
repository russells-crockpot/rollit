"""
"""
import itertools

__all__ = ('reorder_keys',)


def reorder_keys(expected, actual):
    """
    """
    if not isinstance(actual, dict):
        return actual
    result = {}
    for k, expected_value in expected.items():
        actual_value = actual[k]
        if isinstance(expected_value, dict):
            actual_value = reorder_keys(expected_value, actual_value)
        elif isinstance(expected_value, (list, set, tuple)):
            assert len(expected_value) == len(actual_value)
            actual_value = tuple(
                reorder_keys(*z) for z in itertools.zip_longest(expected_value, actual_value))
        result[k] = actual_value
    return result
