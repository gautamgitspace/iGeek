#!/usr/bin/env python

"""
to create a large file, use this:
awk 'BEGIN{for (i = 0; i < 1000000000; i++) {print "123.123.123.123"} }' > t.txt
"""
import subprocess
import time

COMMAND = "split -a 1 -l 500000 t.txt t_"
t0 = time.time()
subprocess.call(COMMAND, shell=True)
t1 = time.time()

print("done. took ~" + str(int(t1-t0))) + " seconds"
