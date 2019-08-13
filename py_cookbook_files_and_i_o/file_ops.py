#!/usr/bin/env python3

import os
import glob
import re
from tempfile import TemporaryFile


top = '/Users/gautam/Desktop'

files = [name for name in os.listdir(top) if os.path.isfile(os.path.join(top, name))]
py_files =  [py_files for py_files in files if py_files.endswith('.py')]
print (py_files)

# search for a file. use of join, and normpath
name = 'amz_tracker.py'
for paths, dirs, files in os.walk(top):
    if name in files:
        full_path = os.path.join(top, paths, name)
        file_abs_path = os.path.normpath(full_path)

# tokenizing different parts of the full path
print (os.path.basename(file_abs_path))
print (os.path.dirname(file_abs_path))
print (os.path.splitext(file_abs_path))

# checking existence
print (os.path.exists(file_abs_path))
print (os.path.isfile(file_abs_path))
print (os.path.isdir(top))

# get metadata
print (os.path.getsize(file_abs_path))
print (os.path.getmtime(file_abs_path))

# another way to get metadata, use glob to search
py_files = glob.glob('/Users/gautam/Desktop/*.py')
meta_data = [(name, os.stat(name)) for name in py_files]
for name, meta in meta_data:
    print (name, meta.st_size, meta.st_mtime)

# fina all modules imported by writing into a temp file
imports = []
with open (file_abs_path, 'rt') as f:
    line = f.readlines()
    for lines in line:
        if lines.startswith('import'):
            with TemporaryFile('w+t') as tf:
                tf.write(str(lines).strip())
                tf.seek(0)
                data = tf.read()
                imports.append(data.split(" ")[1])
print ([modules for modules in reversed(imports)])

# redirect output to a file
name = input('enter your data')
with open ('/Users/gautam/Desktop/data.txt', 'xt') as f:
    f.write(name)
    # clear the file
    f.truncate(0)
