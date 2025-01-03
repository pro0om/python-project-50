from gendiff.parser import get_file_format_and_data
from gendiff.diff import diff
from gendiff.json import format_diff_json


def generate_diff(file_path1, file_path2, formatter='json'):
    data1 = get_file_format_and_data(file_path1)
    data2 = get_file_format_and_data(file_path2)
    difference = diff(data1, data2)
    return format_diff_json(difference, formatter)