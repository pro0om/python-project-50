from pathlib import Path

def get_file_format_and_data(file):
    file_format = Path(file).suffix
    if file_format.lower() == '.json':
        format = 'json'
        data = open(file)
    if file_format.lower() == '.yaml' or file_format.lower() == '.yml':
        format = 'yaml'
        data = Path(file).read_text()
    return data, format