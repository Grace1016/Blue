#!/usr/bin/env python3
"""using debugger to fix the odd script and find the oaks!"""
__author__='Hongye Wang (hw2419@ic.ac.uk)'

import csv
import sys
import doctest
import re

#Define function
def is_an_oak(name):
    """ Returns True if name is starts with 'quercus'
    
    >>> is_an_oak('Fagus sylvatica')
    False
    
    >>> is_an_oak('Quercus robur')
    True
    
    >>> is_an_oak('Quercuss cerris')
    False
    """

    # match 'quercus'
    if re.match('^quercus\s', name, flags=re.I) !=None:
        return True
    else:
       return False


""" main function to find the oak and list the species"""
def main(argv): 
    f = open('../data/TestOaksData.csv','r')
    g = open('../data/JustOaksData.csv','w')
    next(f) # add a header row
    taxa = csv.reader(f)
    csvwrite = csv.writer(g)
    csvwrite.writerow(["Ginus", "Species"])
    oaks = set()
    for row in taxa:
        print(row)
        print ("The genus is: ") 
        print(row[0] + '\n')
        if is_an_oak(row[0] + ' '):
            print('FOUND AN OAK!\n')
            csvwrite.writerow([row[0], row[1]])    

    return 0
    
if (__name__ == "__main__"):
    status = main(sys.argv)

doctest.testmod()