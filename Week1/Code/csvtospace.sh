#!/bin/bash
# Author: Wang Hongye.  hw2419@ic.ac.uk
# Script: csvtospace.sh
# Desc: shell script that takes a comma separated values and converts it to a space separated values file. However, it must not change the input file 
# Arguments: 1-> tab delimited file
# Date: 1st Oct 2018
if [ -z "$1" ]; then
    echo "variable is not set, test file could be found in Data/Temperatures"
else
    echo "creating a space delimited version of $1  "
    cat $1 | tr -s "," " " >> $1.txt
    mv $1.txt ../Results
    echo -e "\nDone!"
    exit
fi