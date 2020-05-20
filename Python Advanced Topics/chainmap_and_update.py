#!/usr/bin/env python3
"""
chainmap: logically combine two different mappings into one. chainmap will
search for key in first, if not found, then in second
"""

from collections import ChainMap

a = {'x' : 1, 'y' : 2}
b = {'y' : 3, 'z' : 4}

c = ChainMap(a, b)

print (c['x'])
print (c['y']) # will find in a and print from a
print (c['z']) # will NOT find in a and search and print from b

print(list(c.keys()))
print(list(c.values()))
print(c.maps)

print ('\n')

merge = dict(a)
merge.update(b)

print(merge['x'])
print(merge['y']) # y will be updated from b 
print(merge['z'])
