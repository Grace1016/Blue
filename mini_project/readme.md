# **CMEE Miniproject

![image](https://user-images.githubusercontent.com/56070370/76150271-685a3e80-60a0-11ea-9b84-eb21395bbca1.png)

**Author:** Hongye Wang (hw2419@ic.ac.uk)

**Description:** A miniproject aims at find the best model for fiting the growth curves. It is a reproducible workflow:wink:.


##Install

#### Python 3.5.2
- pandas: data preparation
- numpy,scipy: numeric and scientific function
- sys: operating system interaction
- lmfit: NLLS
- datatime: timing

#### R 3.2.3
ggplot2: elegant plot

## Running the Miniproject

To run the whole project, just run the script run_MiniProject.sh on the bash shell.

## file structure
'''
Miniproject/
Code:
     find_start_val.ipynb : these .ipynb files are my first drafts in the beginning, after 
     model_fitting.ipynb
     model_function.ipynb
     modify_data.ipynb
     writeup.bib
     writeup.tex 
     find_start_val.py 
     model_fitting.py 
     modelfunction.py 
     modify_data.py 
     best_model_selection.R 
     model_plotting.R 
     run_miniproject.sh 
         

Data:
    LogisticGrowthData.csv 
    LogisticGrowthMetaData.csv
    modified_data.csv
    start_val_data.csv 

Results:
       analysis_dt.csv
       baranyi_model.csv
       buchanan_model.csv
       classical_model.csv
       cubic_model.csv
       gompertz_model.csv
       writeup.pdf
       * images :store some images that the report can use


