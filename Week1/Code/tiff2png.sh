#!/bin/bash

for f in ../Data/*.tif; 
    do  
        echo "Converting $f"; 
        convert "$f"  "$(basename "$f" .tif).jpg"; 
    done
mv "$(basename "$f" .tif).jpg" ../Results