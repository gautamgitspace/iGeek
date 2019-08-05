#!/usr/bin/python

"""
Get  file size, inode, owner of a each file in a given path
Get file permissions, revoke x permissions from all
"""
import subprocess
import os
import fnmatch

COMMAND_LIST_AND_REDIRECT_TO_FILE = "ls -ltrGhi > dir_contents.txt"
p = subprocess.call(COMMAND_LIST_AND_REDIRECT_TO_FILE, shell=True)
p = subprocess.call("sed '1d' dir_contents.txt > tmp.txt", shell=True)

d = {}
fname = "tmp.txt"
if os.path.isfile(fname):
    with open(fname, 'r') as f:
        for line in f:
            tokens = line.strip().split(" ")
            d[tokens[-1].strip()] = tokens[1]
for k,v in d.items():
    print k,v

# revoking x permissions for all dot py files from all the users
for files in os.listdir("."):
    if fnmatch.fnmatch(files, '*.py'):
        subprocess.call("chmod 777" + " " + files, shell=True)
