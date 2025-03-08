import pytest

from gendiff.formatters.plain import format_diff_plain, to_str
from tests.test_utility import get_expected_result, get_input_data


@pytest.mark.parametrize('input_value, expected_value', [
    ("hello", "'hello'"),
    (12, "12"),
    (1.23, "1.23"),
    (True, "true"),
    (False, "false"),
    (None, "null"),
    ({"key": "value"}, "[complex value]"),
    ([1, 2, 3], "[complex value]"),
    ([1, 2, [3, 4]], "[complex value]"),
    ({"key": {"nested_key": "value"}}, "[complex value]"),
    ([], "[complex value]"),
    ({}, "[complex value]")
])
def test_to_str(input_value, expected_value):
    assert to_str(input_value) == expected_value


@pytest.fixture
def input_diff():
    return get_input_data('expected_diff.json')


@pytest.fixture
def expected_result():
    return get_expected_result('expected_plain.txt')


def test_format_diff_plain(input_diff, expected_result):
    assert format_diff_plain(input_diff) == expected_result