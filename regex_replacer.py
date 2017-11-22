#!/usr/bin/python3
'''
REGEX BATCH REPLACEMENT
'''
import argparse
import csv 
import re
from sys import exit


def read_regexp(file):
# reads replacment rules from csv
    try:
        with open(file, 'r') as f:
            re_list = list(csv.reader(f, delimiter=';', quotechar='|'))
    except IOError:
        print("Invalid rules file")
        exit(1)

    return re_list


def read_input(file):
# reads input source
    try:
        with open(file, 'r') as f:
            input_str = f.read()
    except IOError:
        print("Invalid input file")
        exit(1)

    return input_str


def regexp_replace(input_file, output_file, rules):
# applies replacement rules to string
    input = read_input(input_file)
    output = open(output_file, 'w')
    regex_list = read_regexp(rules)

    # search and replace
    for row in regex_list:
        print("replacing", row[0], "with", row[1])
        input = re.sub(row[0], row[1], input)
    
    # write result to output file
    print("write output file")

    try:
        for line in input:
            output.write(line)
        output.close()
    except IOError:
        print("An error occured while writing output file")
        exit(1)
    

    return 0


def main(): 
    parser = argparse.ArgumentParser(description="Transform text input by pre-defined replacment rules")
    required = parser.add_argument_group('required arguments')
    required.add_argument("-f", "--file", dest="input_file", help="define input file", required=True)
    required.add_argument("-o", "--output", dest="output_file", help="define output file", required=True)
    required.add_argument("-r", "--rules", dest="rules", help="define file with replacment rules", required=True)
    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file
    ruleset = args.rules

    regexp_replace(input_file, output_file, ruleset)

    return 0 


if __name__ == '__main__':
    main()




