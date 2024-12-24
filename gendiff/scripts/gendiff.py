import argparse

parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')

parser.add_argument('firs_file',help='')
parser.add_argument('second_file',help='')

parser.add_argument('-f','--format', help='set format to output', default='')

args = parser.parse_args()

print(args)