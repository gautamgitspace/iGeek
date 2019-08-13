#!/usr/bin/python

"""
Remove all the empty directories from a given path
"""
import os
import subprocess

COMMAND_MKDIR = "mkdir"
COMMAND_RMDIR = "rm -rf"

path = "/Users/gautam/Library/Mobile Documents/com~apple~CloudDocs/GitHub Cloud/iGeek/udemy_cracking_the_py_coding_interview"

for i in range(0,10):
    p = subprocess.call(COMMAND_MKDIR + " " + "temp_dir_" + str(i), shell=True)

for i in range(0,10):
    if not os.listdir(path + "/" + "temp_dir_" + str(i)):
        os.rmdir("temp_dir_" + str(i))