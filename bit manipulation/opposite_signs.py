#!/usr/bin/env python
# check if signs of two integers are opposite
def sign_evaluator(a,b):
    return a ^ b < 0
print sign_evaluator(a=3, b=-3)
