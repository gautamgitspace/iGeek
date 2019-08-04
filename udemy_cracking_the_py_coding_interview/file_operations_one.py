#! /usr/bin/env python

"""
Create a directory with name newdirand create a file tempo in the new dir
"""
import os
import subprocess

COMMAND_PWD = "pwd"
COMMAND_MKDIR = "mkdir"
COMMAND_FILE = "touch"

p = subprocess.Popen(COMMAND_PWD, shell = True, stdout=subprocess.PIPE)
out,err = p.communicate()
print "[you are at] " + out

subprocess.call(COMMAND_MKDIR + " newdir", shell = True)
os.chdir("newdir")

p = subprocess.Popen(COMMAND_PWD, shell = True, stdout=subprocess.PIPE)
out,err = p.communicate()
print "[Now you are at] " + out

subprocess.call(COMMAND_FILE + " tempo.txt", shell = True)
