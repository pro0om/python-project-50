import pytest
import json
import os
from gendiff.formatters.stylish import to_str, make_stylish_result



@pytest.mark.parametrize('input_value, expected_value', [
    (None, 'null'),
    (True, 'true'),
    ('string', "string"),
    (1, '1'),
    (2.0, '2.0'),
])
def test_to_str(input_value, expected_value):
    assert to_str(input_value) == expected_value




