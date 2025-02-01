def to_str(value):
    if isinstance(value, (list, dict)):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, int):
        return f"{value}"
    elif value is None:
        return 'null'
    else:
        return str(value)


def make_plain_result_item(item, path=''):
    current_key = item.get('name')
    current_path = f"{path}.{current_key}" if path else current_key
    action = item.get('action')
    new_value = to_str(item.get('new_value'))
    old_value = to_str(item.get('old_value'))

    if action == 'added':
        if path == '':
            return (f"Property {current_path} was added "
                    f"with value: {new_value}")
        return (f"Property in {path} was added {current_key} "
                f"with value: {new_value}")
    elif action == 'deleted':
        if path == '':
            return f"Property {current_path} was removed"
        return f"Property in {path} was removed {current_key}"
    elif action == 'modified':
        return (
            f"Property in {current_path} was updated {current_key}: "
            f"from {old_value} to {new_value}"
        )
    elif action == 'nested':
        children = item.get('children')
        return make_plain_result(children, current_path)
    else:
        return None


def make_plain_result(diff, path=''):
    result = []
    for item in diff:
        formatted_item = make_plain_result_item(item, path)
        if formatted_item is not None:
            result.append(formatted_item)
    return '\n'.join(result)


def format_diff_plain(data):
    return make_plain_result(data)