import json


def json_value(data):
    if not isinstance(data, dict):
        if data == '':
            return None
        else:
            return data
    for key, value in data.items():
        value = json_value(value)
        data[key] = value
    return data


def format_diff_json(diff_result):
    result = json_value(diff_result)
    return json.dumps(result)