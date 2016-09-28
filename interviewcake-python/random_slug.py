#!/usr/bin/env python
# 26+26+10 = 62 and num_chars = 7, this implies 62^7 unique slugs ~ 5 trillion (hmmm. good enough)
import random
def generate_random_slug():
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
  num_chars = 7
  return ''.join([random.choice(alphabet) for char in range(num_chars)])
print generate_random_slug()
