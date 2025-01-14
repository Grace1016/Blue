#!/usr/bin/env python3
""" a test script to print lines in the file 
    and then skip blank lines to print in a file """

__author__=' Hongye Wang (hw2419@ic.ac.uk) '

#############################
# FILE INPUT
#############################
# Open a file for reading
f = open('../sandbox/test.txt', 'r')
# use "implicit" for loop:
# if the object is a file, python will cycle over lines
for line in f:
    print(line)

# close the file
f.close()

# Same example, skip blank lines
f = open('../sandbox/test.txt', 'r')
for line in f:
    if len(line.strip()) > 0:
        print(line)

f.close()



