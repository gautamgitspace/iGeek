#!/usr/bin/python
'''
Python decorators

Functions and methods are called callable as they can be called.
In fact, any object which implements the special method __call__() is
termed callable. So, in the most basic sense, a decorator is a callable
that returns a callable.

below example shows both closures and decorators

make_pretty is a decorator here as it takes ordinary as an arg and adds some
functionality to it (pimps it basically). It's callable as well as returns a
callable i.e. make_pretty_internal()
'''

def make_pretty(func):
    def make_pretty_internal():
        print "BUT I GOT MORE PIMPED"
        func()
    return make_pretty_internal

def ordinary():
    print "I AM ORDINARY"

# makes division smarter by adding divide by zero check
def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

now_pretty = make_pretty(ordinary)
now_pretty()

@smart_divide
def divide(a,b):
    return a/b

divide(2,5)

'''
above can also be done by:

divide_this = smart_divide(divide)
print divide_this(2,5)

when using @, def of 'ordinary' method has to follow the @ decelaration

'''
