#!/usr/bin/env python
import sys
def add_and_check_overflow(n1, n2):
    if n1 > (sys.maxsize - n2):
        return True
    else:
        return n1 + n2
print 'isOverflow?', add_and_check_overflow(sys.maxsize, 10)
