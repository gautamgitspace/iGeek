# simply walk through the stack and find the max element.
#This takes O(n) time for each call to get_max()
from Stack import *
class MaxStack:
     def __init__(self):
         self.base = Stack()
         self.max = Stack()
     def peek(self):
        if not self.base: return None
        return self.base[len(self.base)-1]
     def push(self, item):
        if item >= self.max.peek():
            self.max.push(item)
        self.base.push(item)
     def pop(self):
         val = self.base.pop()
         if (val == self.max.peek()):
             self.max.pop()
         return val
     def getmax(self):
         return self.max.peek()


s=MaxStack()

s.push(4)
s.push(5)
s.push(6)
max1 = s.getmax()
print "max after pushing 4,5 and 6: ", max1
s.push(8)
max2 = s.getmax()
print "max after pushing 8 now: ", max2
print max2
print(s.pop())
print(s.pop())
max3 = s.getmax()
print "max after popping 2 elements: ", max3

