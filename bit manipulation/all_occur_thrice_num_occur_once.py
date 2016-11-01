#!/usr/bin/env python
#all numbers appear thrice except one number that appears once
def single(array):
    ones, twos = 0, 0
    for x in array:
        #bits that are both in ones and array[i] add them to twos using bitwise OR
        twos |= (ones & x)
        #bitwise XOR previous bits with new one to get odd occurrences
        ones ^= x
        #bits that appear the third time should not be in ones and twos so take complement
        not_threes = ~(ones & twos)
        #remove common bits from ones
        ones &= not_threes
        #remove common bits from twos
        twos &= not_threes
    return ones
print "Number that occurs once:", single(array=[1,1,1,2,2,2,3,5,3,3])
