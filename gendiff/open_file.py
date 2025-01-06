from pathlib import Path


def get_file_format_and_data(file):
    file_path = Path(file)
    if file_path.suffix.lower() == '.json':
        format = 'json'
        data = open(file)
    return data, format