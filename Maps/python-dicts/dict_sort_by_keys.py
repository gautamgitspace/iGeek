#!/usr/bin/env python
import operator
fname = "/Users/abhigaut/Library/Mobile Documents/com~apple~CloudDocs/GitHub Cloud/iGeek/Maps/python-dicts/phones.txt"
fileHandle = open(fname)
map = {}
for line in fileHandle:
    token = line.strip().split(',')
    if token[3] not in map:
        map[token[3]] = int(token[2])
for items in reversed(sorted(map.items())):
    print items
