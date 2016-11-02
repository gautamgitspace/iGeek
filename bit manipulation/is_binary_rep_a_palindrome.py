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
def check_palindrome(array):
    if array == array[::-1]:
        return 'Yikes! This is a Palindrome Binary Shit.'
    else:
        return 'No! This is not a Palindrome Binary Shit.'
print bin_rep(number=21)
print check_palindrome(bin_rep(21))
