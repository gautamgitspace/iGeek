#! /usr/bin/env Python
"""
Rename  a file in a particular director Take the backup before renaming
NOTE - run after file_operations_one.py
"""
import subprocess
import os

COMMAND_RENAME = "mv"
COMMAND_MAKE_A_COPY = "cp"
COMMAND_PWD = "pwd"

dir = "/Users/abhigaut/Library/Mobile Documents/com~apple~CloudDocs/GitHub Cloud/iGeek/udemy_cracking_the_py_coding_interview/newdir/"
file = "tempo.txt"
file_new = "tempo2.txt"
file_copy = "tempo_copy.txt"
if os.path.isdir(dir):
    os.chdir(dir)
    if os.path.isfile(file):
        p = subprocess.call(COMMAND_MAKE_A_COPY + " " + file + " " + file_copy, shell=True)
        p = subprocess.Popen(COMMAND_RENAME + " " + file + " " + file_new, shell=True)
    else:
        print "No such file or directory - " + file
