#!/usr/bin/env python3
"""this is a script to run fmr.R"""

__author__ = 'Hongye Wang (hw2419@ic.ac.uk)'

import subprocess
p = subprocess.Popen("Rscript fmr.R", stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
stdout, stderr = p.communicate()
print(stdout.decode())