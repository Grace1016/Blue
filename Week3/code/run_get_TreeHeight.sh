# !/bin/bash
# Author: Hongye Wang (hw2419@ic.ac.uk)
# Script: run_get_TreeHeight.sh
# Desc: text get_TreeHeight.R, get_TreeHeight.py in unix
# Arguments: none
# Date: Oct 2019

# text get_TreeHeight.R
Rscript get_TreeHeight.R ../data/trees.csv

# text get_TreeHeight.py
ipython3 get_TreeHeight.py ../data/trees.csv