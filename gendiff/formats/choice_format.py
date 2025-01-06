from gendiff.formats.json import format_diff_json


def format_diff(diff, format):
    if format == 'json':
        return format_diff_json(diff)
    else:
        raise ValueError(f"Unsupported formatter: {format}")