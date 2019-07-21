#!/usr/bin/python

import copy

'''
SHALLOW COPY PLAYGROUND

A shallow copy creates a new object which stores the reference of the
original elements. So, a shallow copy doesn't create a copy of nested
objects, instead it just copies the reference of nested objects.
This means, a copy process does not recurse or create copies of nested
objects itself.
'''

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

new_list = old_list

print id(old_list)
print id(new_list)
print("\n")

new_list = copy.copy(old_list)

print id(old_list)
print id(new_list)
print("\n")

old_list.append([4,4,4])

print old_list
print new_list
print("\n")

old_list[1][1] = "AA"

print old_list
print new_list
print("\n")

'''
DEEP COPY PLAYGROUND

A deep copy creates a new object and recursively adds the copies of
nested objects present in the original elements.
'''
old_list_deep =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list_deep = copy.deepcopy(old_list_deep)

print old_list_deep
print new_list_deep
print("\n")

old_list_deep[1][1] = "BB"

print old_list_deep
print new_list_deep
