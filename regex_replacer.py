#!/usr/bin/python3
'''
REGEXP BATCH REPLACEMENT
'''

import csv 
import re
from sys import exit

regex_file = 'FILENAME'  # specify csv with regex rules, default delimiter = ';', quotechar = '|'
input_file = 'FILENAME'  # source file
output_file = 'FILENAME' # output file


def read_regexp(file=regex_file):
	'''reads regex replacement rules into list'''
    try:
        with open(file, 'r') as f:
            re_list = list(csv.reader(f, delimiter=';', quotechar='|'))
    except FileNotFoundError:
        print("invalid regex file")
        raise
        exit(1)

    return re_list


def read_input(file = input_file):
	'''reads input source'''
    try:
        with open(file, 'r') as f:
            input_str = f.read()
    except FileNotFoundError:
        print("invalid input file")
        raise
        exit(1)

    return input_str


def regexp_replace(file_out = output_file):
	'''applies replacements in input file and writes result to ouput'''

    input = read_input()
    output = open(file_out, 'w')
    regex_list = read_regexp()

    # search and replace
    for row in regex_list:
        print("replacing", row[0], "with", row[1])
        input = re.sub(row[0], row[1], input)

    # write result to output file
    print("write output file")
    for line in input:
        output.write(line)

    output.close()
    return 0


regexp_replace()






