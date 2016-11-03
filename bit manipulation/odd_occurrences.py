#!/usr/bin/env python
#this is same as the missing_drone/all numbers occur twice, one number occurs once problem
def find_odd_occurrence(array):
    res = 0;
    for item in array:
        res ^= item
    return res
print "Number occuring odd times:", find_odd_occurrence(array=[1,1,2,4,5,4,5,2,6,7,7,6,45,45,4])
