import os

import pytest

from gendiff.generate_diff import generate_diff
from tests.test_utility import get_expected_result


@pytest.mark.parametrize('file3_name, file4_name, formatter', [
    ('file3.json', 'file4.json', 'stylish'),
    ('file3.yml', 'file4.yml', 'stylish'),
    ('file3.json', 'file4.json', 'plain'),
    ('file3.yml', 'file4.yml', 'plain'),
    ('file3.json', 'file4.json', 'json'),
    ('file3.yml', 'file4.yml', 'json')
])
def test_generate_diff(file3_name, file4_name, formatter):
    file1_path = os.path.join('tests', 'fixtures', f'{file3_name}')
    file2_path = os.path.join('tests', 'fixtures', f'{file4_name}')
    expected_result = get_expected_result(f'expected_{formatter}.txt')
    actual_result = generate_diff(file1_path, file2_path, formatter)
    assert actual_result == expected_result

