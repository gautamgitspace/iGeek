#!/usr/bin/python

'''
Python closures
conditions to be met:

- We must have a nested function (function inside a function).
- The nested function must refer to a value defined in the enclosing function.
- The enclosing function must return the nested function.

'''
def make_multipliers_of(x):
    def multiplier(n):
        return x * n
    return multiplier

table_of_three = make_multipliers_of(3)
table_of_five = make_multipliers_of(5)
table_of_six = make_multipliers_of(6)

print table_of_three(2)
print table_of_five(2)
print table_of_six(2)
