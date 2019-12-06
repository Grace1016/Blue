#!/usr/bin/env python3
"""This is a script to lists if files and direcyories from home directory"""

__author__ = 'Hongye Wang'

# Use the subprocess.os module to get a list of files and  directories 
# in your ubuntu home directory 

# Hint: look in subprocess.os and/or subprocess.os.path and/or 
# subprocess.os.walk for helpful functions

import subprocess

#################################
#~Get a list of files and 
#~directories in your home/ that start with an uppercase 'C'

# Type your code here:

# Get the user's home directory.
home = subprocess.os.path.expanduser("~")

# Create a list to store the results.
FilesDirsStartingWithC = []

# Use a for loop to walk through the home directory.
d = 0
f = 0
for (dir, subdir, files) in subprocess.os.walk(home):
    for directory in dir:
        if directory.startswith("C"):
            d = d + 1
            FilesDirsStartingWithC.append(directory)
    for file in files:
        if file.startswith("C"):
            f = f + 1
            FilesDirsStartingWithC.append(file)
print("files and dirs start with 'C': directory number:", d, "; file number:", f, "\n\n", FilesDirsStartingWithC,"\n\n")
            

#################################
# Get files and directories in your home/ that start with either an 
# upper or lower case 'C'

# Type your code here:
a = 0
b = 0
FilesDirsStartingWithc = []
for (dir, subdir, files) in subprocess.os.walk(home):
    for directory in subdir:
        if directory.lower().startswith("c"):
            a = a + 1
            FilesDirsStartingWithc.append(directory)
    for file in files:
        if file.lower().startswith("c"):
            b = b + 1
            FilesDirsStartingWithc.append(file)
print("files and dirs start with 'C' or 'c': directory number:", a, "; file number:", b, "\n\n", FilesDirsStartingWithc,"\n\n")
#################################
# Get only directories in your home/ that start with either an upper or 
#~lower case 'C' 

# Type your code here:
c = 0
DirsStartingWithc = []
for (dir, subdir, files) in subprocess.os.walk(home):
    for directory in subdir:
        if directory.lower().startswith("c"):
            c = c + 1
            DirsStartingWithc.append(directory)
print("only dirs start with 'C': directory number:", c, "\n\n", DirsStartingWithc)