#!/usr/bin/env python
#Find the largest and the smallest number in a list. The list is stored in two parts, ascending and then descending.

def smallest(list):
    if list[0] > list[len(list)-1]:
        return list[len(list)-1]
    else:
        return list[0]

def largest(list):
    l = 0
    r = len(list)-1
    while(l<r):
        middle = (l+r)/2
        if list[middle] > list[middle-1]:
            l=middle
        if list[middle] > list[middle+1]:
            r=middle

    return list[middle]

lst = [2,3,17,19,21,25,27,29,33,36,35,22,7,1]
print 'SMALLEST:', smallest(lst)
print 'LARGEST:', largest(lst)
