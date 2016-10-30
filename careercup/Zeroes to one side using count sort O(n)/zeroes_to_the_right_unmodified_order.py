#!/usr/bin/env python
def zeroes_to_the_right(array):
    count = 0
    for item in array:
        if item != 0:
            array[count] = item
            count+=1
    print 'COUNT:', count
    print 'len of array:', len(array)
    while(count < len(array)):
            array[count] = 0
            count+=1
    return array

print zeroes_to_the_right(array=[2,0,3,1,0,0,0,0,0,0,4,5,0])
