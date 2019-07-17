#!/usr/bin/python
'''
Iterator in Python is simply an object that can be iterated upon.
An object which will return data, one element at a time.

They are hidden in the implementation of for loops for instance.
'''

class Example:
    def __iter__(self):
        self.num = 1
        return self
    def next(self):
        num = self.num
        self.num += 2
        return num

if __name__ == "__main__":
    a = iter(Example())
    print next(a)
    print next(a)
