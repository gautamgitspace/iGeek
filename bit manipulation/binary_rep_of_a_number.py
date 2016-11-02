#!/usr/bin/env python
#binary representation of a given number
def bin_rep(number):
    lst = []
    while(number):
        if number&1 == 1:
            lst.append(str(1))
        else:
            lst.append(str(0))
        number = number >> 1
    return ' '.join(reversed(lst))
print bin_rep(number=7)
