import os


def get_file_format(file_path):
    _, ext = os.path.splitext(file_path)
    return ext[1:]


def get_file_data(file_path):
    with open(file_path) as file:
        return file.read()