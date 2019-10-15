#!/usr/bin/env python3
"""Description of this program or application.
    You can use several lines"""
__author__='Wang Hongye (hw2419@ic.ac.uk)'

## imports ##
import sys # module to interface our program with the operating system

## constants ##

## functions ##
def main(argv):
    """ Main entry point of the program """
    print('This is a boilerplate') # NOTE: indented using two tabs or 4 spaces
    return 0

if __name__ == "__main__": 
    """Makes sure the "main" function is called from command line"""  
    status = main(sys.argv)
    sys.exit(status)