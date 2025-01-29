import pytest
import os
from gendiff.formatters import stylish, plain, json


@pytest.fixture()
def given_diff():
    fixture_path = os.path.join('tests', 'fixtures', 'exp1_given_diff.txt')
    with open(fixture_path) as file:
        return file.read()

def test_stylish_format(given_diff):
    with open('tests/fixtures/exp1_stylish.txt', 'r') as result:
        assert stylish.format_diff_stylish(given_diff) == result.read()


def test_plain_format(given_diff):
    with open('tests/fixtures/exp1_plain.txt', 'r') as result:
        assert plain.format_diff_plain(given_diff) == result.read()


def test_json_format(given_diff):
    with open('tests/fixtures/exp1_json.txt', 'r') as result:
        assert json.format_diff_json(given_diff) == result.read()