#!/usr/bin/env python3
""" a test script to save the elements of a list to a file """
__author__=' Hongye Wang (hw2419@ic.ac.uk) '

#############################
# FILE OUTPUT
#############################
# Save the elements of a list to a file
list_to_save = range(100)

f = open('../sandbox/testout.txt','w')
for i in list_to_save:
    f.write(str(i) + '\n') ## Add a new line at the end

f.close()