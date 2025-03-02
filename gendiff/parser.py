import json

import yaml

from gendiff.io import get_file_data, get_file_format


def parse_data(content, format):
    if format == 'json':
        return json.loads(content)
    if format in ['yml', 'yaml']:
        return yaml.safe_load(content)


def parse_data_from_file(file_path):
    format = get_file_format(file_path)
    data = get_file_data(file_path)
    return parse_data(data, format)