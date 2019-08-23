#!/usr/bin/env python

"""
using map and reduce:
map and reduce both take an function and iterable
function will operate on elements of the iterable
"""
from functools import reduce

def pow_of_two(n):
    return 2**n

nums = [0,1,2,3,4,5]
res = map(pow_of_two, nums)
print res

# same stuff can be done using lambdas

res = map(lambda x: 2**x, nums)
print res

# what about reduce?
print reduce(lambda x,y: x+y, nums)

# this will throw error:
# print reduce(pow_of_two, nums)
"""
Traceback (most recent call last):
  File "./Python Advanced Topics/map.py", line 24, in <module>
    print reduce(pow_of_two, nums)
TypeError: pow_of_two() takes exactly 1 argument (2 given)
"""

# so will this:
# sprint reduce(lambda x: x+y, nums)
"""
Traceback (most recent call last):
  File "./Python Advanced Topics/map.py", line 27, in <module>
    print reduce(lambda x: x+y, nums)
TypeError: <lambda>() takes exactly 1 argument (2 given)
"""
