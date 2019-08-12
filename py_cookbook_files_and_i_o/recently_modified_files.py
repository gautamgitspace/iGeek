#!/usr/bin/env python3

import os
import time

def stalker(top, seconds):
    now = time.time()
    if os.path.exists(top):
        for path, dirs, files in os.walk(top):
            for file_names in files:
                fn_full_path = os.path.join(path,file_names)
                mod_time = os.path.getmtime(fn_full_path)
                if mod_time > now - seconds:
                    print (fn_full_path)

if __name__ == "__main__":
    stalker("/Users/abhigaut/Desktop/", 180)
