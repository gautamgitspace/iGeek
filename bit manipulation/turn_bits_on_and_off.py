#!/usr/bin/env python
#turn kth bit on or off
def turn_k_off(number, bit):
    return (number & ~(1 << (bit - 1)))
def turn_k_on(number, bit):
    return(number | (1 << (bit -1)))
print turn_k_off(number=7, bit=4)
print turn_k_on(number=8, bit=1)
