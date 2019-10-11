#!/bin/bash
# Author: Wang Hongye hw2419@ic.ac.uk
# Script: tabtocsv.sh
# Desc: substitute the tabs in the files with commas
# Arguments: 1-> tab delimited file
# Date: Oct 2019
var=${1:-../SandBox/test.txt} # set a default value if $1 unset
echo "Creating a comma delimited version of $var ..."
cat $var | tr -s "\t" "," >> $var.csv
mv $var.csv ../Results
echo -e "\nDone!"
exit