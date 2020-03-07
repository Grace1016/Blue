#!/bin/bash
#Description: run CMEE miniproject
#############################################################################
echo "No.1"
echo " modify_data.py"
python3 modify_data.py

echo "No.2"
echo " find_start_val.py"
python3 find_start_val.py

echo "No.3"
echo " model_function"
python3 modelfunction.py

echo "No.4"
echo " model_fitting.py"
python3 model_fitting.py

echo "No.5"
echo " best_model_selection.R"
Rscript best_model_selection.R

echo "No.6"
echo " model_plotting.R"
Rscript model_plotting.R


echo " compile pdf of report "

pdflatex writeup.tex 
pdflatex writeup.tex 
bibtex writeup       
pdflatex writeup.tex 
pdflatex writeup.tex 

mv writeup.pdf ../results/

# delete all the rubbish
rm -f *~
rm -f *.aux
rm -f *.blg
rm -f *.log
rm -f *.nav
rm -f *.out
rm -f *.snm
rm -f *.toc
rm -f *.vrb
rm -f *.bbl
rm -f *.dvi
rm -f *.lot
rm -f *.lof

echo ""
echo "################################################ finished! ##################################################"




