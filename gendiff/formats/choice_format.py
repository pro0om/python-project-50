from gendiff.formats.json import format_diff_json
from gendiff.formats.stylish import format_diff_stylish
from gendiff.formats.plain import format_diff_plain


def format_diff(diff, format):
    if format == 'json':
        return format_diff_json(diff)
    if format == 'stylish':
        return format_diff_stylish(diff)
    if format == 'plain':
        return format_diff_plain(diff)
    else:
        raise ValueError(f"Unsupported formatter: {format}")