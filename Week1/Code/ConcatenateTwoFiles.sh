#!/bin/bash
if [ $# -ne 3 ]; then # return an error message if the inputs are not correct
    echo "variables is not set completely"
else
    cat $1 > $3
    cat $2 >> $3
    echo "Merged File is"
    cat $3
fi