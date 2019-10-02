#!/bin/bash
# Author: Wang Hongye.  hw2419@ic.ac.uk
# Script: csvtospace.sh
# Desc: shell script that takes a comma separated values and converts it to a space separated values file. However, it must not change the input file 
# Arguments: 1-> tab delimited file
# Date: 1st Oct 2018

echo "a,b,c,d,e" | tr -s "," " "
exit