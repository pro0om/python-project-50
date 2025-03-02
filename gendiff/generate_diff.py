from gendiff.diff import diff
from gendiff.formatters.choice_format import format_diff
from gendiff.parser import parse_data_from_file


def generate_diff(file_path1, file_path2, format='stylish'):
    dict1 = parse_data_from_file(file_path1)
    dict2 = parse_data_from_file(file_path2)
    difference = diff(dict1, dict2)
    return format_diff(difference, format)

