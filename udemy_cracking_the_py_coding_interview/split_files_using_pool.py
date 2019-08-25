#!/usr/bin/env python3
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
    for i in range (0,100000):
        os.system("echo 'Sic Mundus Creatus Est' >> foo.txt")
    # make copies 100 of foo by invoking this
    subprocess.call(['./file_cp.sh'])

def files_to_act_on():
    files_to_process = glob.glob(dir_path + '/doo*.txt')
    return files_to_process

def worker(big_file):
    """
    splits one big file into small files
    """
    os.system("split -a 3 -l 2500 " + big_file + " " + big_file + "_t_")

with futures.ProcessPoolExecutor() as pool:
    pool.submit(dumper)

ftop = files_to_act_on()

with futures.ProcessPoolExecutor() as pool:
    pool.map(worker, ftop)

t2 = time.time()
print ('done. took ~' + str(t2-t1) + ' seconds')
