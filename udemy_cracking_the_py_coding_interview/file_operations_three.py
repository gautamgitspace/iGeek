#!/usr/bin/env Python
"""
List all the files from a given path and verify the file test.txt file exists
"""
import subprocess
import os

COMMAND_LIST = "ls -ltraGh"

file = "tempo.txt"
path = "/Users/abhigaut/Library/Mobile Documents/com~apple~CloudDocs/GitHub Cloud/iGeek/udemy_cracking_the_py_coding_interview/newdir"

if os.path.isdir(path):
    os.chdir(path)

p = subprocess.Popen(COMMAND_LIST, shell=True, stdout=subprocess.PIPE)
out = p.communicate()
print out

if os.path.isfile(file):
    print "File " + file + " exists"
