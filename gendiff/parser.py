from pathlib import Path
import json


def get_file_format_and_data(file):
    file_path = Path(file)
    if file_path.suffix.lower() != '.json':
        raise ValueError(f'Unsupported file format: {format}')
    if file_path.suffix.lower() == '.json':
        format = 'json'
        data = open(file)
    return data, format

def parser(data, format: str):
    return json.load(data)

