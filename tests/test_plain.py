import pytest
import os
import json
from gendiff.formatters.plain import to_str, make_plain_result


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



def read_file(file_name):
    fixture_path = os.path.join('tests', 'fixtures', f'{file_name}')
    with open(fixture_path) as file:
        return file.read()

@pytest.fixture
def input_diff():
    return json.loads(read_file('exp1_given_diff.json'))
@pytest.fixture
def expected_result():
    return read_file('exp1_plain.txt')


def test_make_plain_result(input_diff, expected_result):
    assert make_plain_result(input_diff) == expected_result