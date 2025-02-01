import os
import json


def read_file(file_name):
    path_to_fixtures = os.path.join('tests', 'fixtures', f'{file_name}')
    with open(path_to_fixtures) as file:
        return file.read()


def get_input_data(file_name):
    return json.loads(read_file(file_name))


def get_expected_result(file_name):
    return read_file(file_name)