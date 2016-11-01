#!/usr/bin/env python
#swap a number in place(that is, without temporary vairables)

#via arithmetic
def swap(number_one, number_two):
    number_one = number_one - number_two #9-4=5
    number_two = number_one + number_two #5+4=9
    number_one = number_two - number_one

    print 'number_one:', number_one
    print 'number_two:', number_two


#via bit manipulation
def swap_alternate(number_one, number_two):
    number_one ^= number_two
    number_two ^= number_one
    number_one ^= number_two

    print 'number_one:', number_one
    print 'number_two:', number_two

number_one, number_two = map(int, raw_input('Enter two numbers seprated by a space: ').split())
swap(number_one, number_two)
swap_alternate(number_one, number_two)
