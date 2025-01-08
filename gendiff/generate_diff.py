from gendiff.open_file import get_file_format_and_data
from gendiff.parser import parser
from gendiff.diff import diff
from gendiff.formats.choice_format import format_diff


def generate_diff(file_path1, file_path2, format='stylish'):
    data1, format1 = get_file_format_and_data(file_path1)
    data2, format2 = get_file_format_and_data(file_path2)
    dict1 = parser(data1, format1)
    dict2 = parser(data2, format2)
    difference = diff(dict1, dict2)
    return format_diff(difference, format)