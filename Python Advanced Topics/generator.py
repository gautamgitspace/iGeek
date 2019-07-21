#!/usr/bin/python
'''
Python generators are a simple way of creating iterators. All the overhead
such as implementing iter() and next() routines are automatically handled
by generators in Python.

WHY USE THEM:
- less overhead
- intuitive
- take less memory as a normal function to return a sequence will have to
first create the entire sequence in the Memory
- supports piplelining (list comprehension)
'''
def pow_of_two(max):
    n = 0
    while (n < max):
        yield 2 ** n
        n += 1
def rev_string(text):
    for i in range (len(text)-1, -1, -1):
        yield text[i]

if __name__ == "__main__":
    # will just print what 'yield' yields
    print next(pow_of_two(10))
    print "\n"
    # will dump everything as pow_of_two routine is an iterator obj
    for items in pow_of_two(10):
        print items
    # will reverse the string
    for items in rev_string("hello"):
        print items
