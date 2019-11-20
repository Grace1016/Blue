#!/usr/bin/env python3
"""This is a script to run R in python"""

__author__ = 'Hongye Wang (hw2419@ic.ac.uk)'

import subprocess
subprocess.Popen("Rscript --verbose TestR.R > ../result/TestR.Rout 2> ../result/TestR_errFile.Rout",shell=True).wait()
