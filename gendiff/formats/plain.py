
def to_str(value):
    if isinstance(value, (list, dict)):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, int):
        return value
    elif value is None:
        return 'null'
    else:
        return str(value)

    def make_plain_result(item, path=''):
        action = item['action']
        result = ''
        for key, value in item.items():
            current_path = f"{path}{value['key']}"
            if action == 'changed':
                result += (f"Property '{current_path}' was updated. "
                           f"From {plain_value(value['old'])} to {plain_value(value['new'])}\n")
            elif action == 'removed':
                result += f"Property '{current_path}' was removed\n"
            elif action == 'added':
                result += f"Property '{current_path}' was added with value: {plain_value(value['value'])}\n"
            elif action == 'nested':
                result += make_plain_result(value['value'], current_path + '.') + '\n'
        return result[:-1]

def format_diff_plain(data):
    return make_plain_result(data, path)