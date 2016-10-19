#!/usr/bin/env python
def find_elements(array, sum):
    a = set()
    b = []
    for item in array:
        second_number = sum - item
        if second_number in a:
            b.append(second_number)
            b.append(item)
        else:
            a.add(item)
    return b


array = [1,6,2,4,5,56,33,3,4]
print find_elements(array, 7)
