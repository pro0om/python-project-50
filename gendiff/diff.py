def common_and_different(dict1, dict2):
    common = dict1.keys() & dict2.keys()
    removed = dict1.keys() - dict2.keys()
    added = dict2.keys() - dict1.keys()
    return common, removed, added

def for_add(key, value):
    return {
        'action': 'added',
        'name': key,
        'new_value': value
    }


def for_delete(key, value):
    return {
        'action': 'deleted',
        'name': key,
        'old_value': value
    }


def for_unchanged(key, value):
    return {
        'action': 'unchanged',
        'name': key,
        'value': value
    }


def for_changed(key, value1, value2):
    return {
        'action': 'modified',
        'name': key,
        'new_value': value2,
        'old_value': value1
    }


def for_nested(key, value1, value2):
    return {
        'action': 'nested',
        'name': key,
        'children': diff(value1, value2)
    }


def diff(dict1, dict2):
    keys = dict1.keys() | dict2.keys()
    common, removed, added = common_and_different(dict1, dict2)
    result = []

    for key in keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)

        if key in added:
            result.append(for_add(key, value2))
        elif key in removed:
            result.append(for_delete(key, value1))
        elif key in common and value1 == value2:
            result.append(for_unchanged(key, value1))
        elif all(
            [key in common,
             value1 != value2,
             isinstance(value1, dict),
             isinstance(value2, dict)]
        ):
            result.append(for_nested(key, value1, value2))
        else:
            result.append(for_changed(key, value1, value2))

    sorted_diff_result = sorted(result, key=lambda x: x['name'])

    return sorted_diff_result





