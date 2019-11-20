#!/usr/bin/env python3
"""This script is to run LV* script and the profile them."""

__author__ = 'Hongye Wang (hw2419@ic.ac.uk)'

import subprocess
import time

start = time.time()
subprocess.os.system("python3 LV1.py")
print("LV1.py takes %f s to run" % (time.time() - start))

start = time.time()
subprocess.os.system("python3 LV2.py 1.0 0.5 1.5 0.75 40")
print("LV2.py takes %f s to run" % (time.time() - start))

start = time.time()
subprocess.os.system("python3 LV3.py 1.0 0.1 0.5 0.75 20")
print("LV3.py takes %f s to run" % (time.time() - start))

start = time.time()
subprocess.os.system("python3 LV4.py 1.0 0.1 0.5 0.75 20")
print("LV4.py takes %f s to run" % (time.time() - start))