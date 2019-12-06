#!/bin/bash
# Script: cp_cpt_speed.sh
# Author:Hongye Wang (hw2419.ic.ac.uk)
# Desc: Compare computational speed in four script
# Date: Dec 2019

echo -e "Comparing the computational speed in loop and vectorize namely when running Vectorize1.R \n"
Rscript Vectorize1.R 

echo -e  "\n Comparing the computational speed in loop and vectorize when running Vectorize1.py \n"
python3 Vectorize1.py

echo -e "\n Comparing the computational speed in loop and vectorize when running Vectorize2.py \n"
Rscript Vectorize2.R

echo -e "\n Comparing the computational speed in loop and vectorize when running Vectorize2.py \n"
python3 Vectorize2.py

echo -e "\n In summary, the computational speed in loop are much slower that that in using vectorize!"