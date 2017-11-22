# regexp_replacer
Small Python3 script to apply multiple regex replacement rules on text streams

1. Replacement rules can be defined in a single csv file.
Please note the default delimiter = ';' and quotechar = '|'.

Example: 
|EXPRESSION|;|REPLACEMENT| 

2. Run script with specified input, output and rule file. 
usage: regex_replacer.py [-h] -f INPUT_FILE -o OUTPUT_FILE -r RULES

