import pytest
import os
import json
from gendiff.formatters.plain import to_str, make_plain_result
from tests.support_test import get_expected_result, get_verifiable_data

@pytest.mark.parametrize('input_value, expected_value', [
    ("hello", 'hello'),
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



