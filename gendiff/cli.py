import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')

    parser.add_argument('firs_file',help='')
    parser.add_argument('second_file',help='')
    parser.add_argument('-f','--format', help='Set format to output',
                         default='', type=str)

    args = parser.parse_args()

    return args