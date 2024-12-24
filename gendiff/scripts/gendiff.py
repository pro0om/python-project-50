import argparse

parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')

parser.add_argument('firs_file',help='Path to file')
parser.add_argument('second_file',help='Path to file')
args = parser.parse_args()

print(args)