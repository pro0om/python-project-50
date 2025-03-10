import pytest

from gendiff.formatters.stylish import format_diff_stylish, to_str
from tests.test_utility import get_expected_result, get_input_data


@pytest.mark.parametrize('input_value, expected_value', [
    (None, 'null'),
    (True, 'true'),
    ('string', "string"),
    (1, '1'),
    (2.0, '2.0'),
])
def test_to_str(input_value, expected_value):
    assert to_str(input_value) == expected_value


@pytest.fixture
def input_diff():
    return get_input_data('expected_diff.json')


@pytest.fixture
def expected_result():
    return get_expected_result('expected_stylish.txt')


def test_format_diff_stylish(input_diff, expected_result):
    assert format_diff_stylish(input_diff) == expected_result



