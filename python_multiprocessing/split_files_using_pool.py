#!/usr/bin/env python3

"""
template to achieve parallel programming
using process pool executor and put it to
use to fabricate a file loaded with text
using 'dumper' and then to split it into
small files using the routine 'worker'

as we know from pool_playground.py:
pool.map() - takes a fn & an *iter as args
pool.submit() - takes a fn & *args
"""

import os
import time
from concurrent import futures
import subprocess
import re
import glob

t1 = time.time()
dir_path = '/Users/abhigaut/Desktop'

def dumper():
    os.system("echo '$' > foo.txt")
    for i in range (0,10000):
        os.system("echo 'Sic Mundus Creatus Est' >> foo.txt")
    # make copies 100 of foo by invoking this
    subprocess.call(['./file_cp.sh'])

def files_to_act_on():
    return glob.glob(dir_path + '/doo*.txt')

def worker(big_file):
    os.system("split -a 3 -l 2500 " + big_file + " " + big_file + "_t_")

with futures.ProcessPoolExecutor() as pool:
    pool.submit(dumper)

ftop = files_to_act_on()

with futures.ProcessPoolExecutor() as pool:
    pool.map(worker, ftop)

t2 = time.time()
print ('done. took ~' + str(t2-t1) + ' seconds')
