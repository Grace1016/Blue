#!/usr/bin/env python3
"""This script extract information about some species in a file by using regex."""

__author__ = 'Hongye Wang (hw2419@ic.ac.uk)'

import re
import numpy as np
# Read the file
f = open('../Data/blackbirds.txt', 'r')
text = f.read()
f.close()

# remove \t\n and put a space in:
text = text.replace('\t',' ')
text = text.replace('\n',' ')

# note that there are "strange characters" (these are accents and
# non-ascii symbols) because we don't care for them, first transform
# to ASCII:
text = text.encode('ascii', 'ignore').decode() #will not work in python 3

# Now extend this script so that it captures the Kingdom, 
# Phylum and Species name for each species and prints it out to screen neatly.

# Hint: you may want to use re.findall(my_reg, text)...
# Keep in mind that there are multiple ways to skin this cat! 
# Your solution may involve multiple regular expression calls (easier!), or a single one (harder!)
# blackbirds = re.findall(r'(Kin\w+\s+\w+)|(Phy\w+\s+\w+)|(Spe\w+\s+\w+)',text)
# for blackbird in blackbirds:
    # print(blackbird)

Kingdoms = re.findall(r'Kin\w+\s+\w+',text)
Phylums = re.findall(r'Phy\w+\s+\w*',text)
Species = re.findall(r'Spe\w+\s+\w+',text)

a = np.array(Kingdoms)
b = np.array(Phylums)
c = np.array(Species)
blackbirds = np.column_stack((a,b,c))
print(blackbirds)