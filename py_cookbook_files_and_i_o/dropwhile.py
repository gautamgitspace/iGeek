#!/usr/bin/env python3

from itertools import dropwhile

fpath = '/Users/abhigaut/Desktop/utils-py/decimal_to_hex.py'
with open(fpath) as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print (line, end=' ')
