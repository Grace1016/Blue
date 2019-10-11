#!/bin/bash
if [ -z "$1"]; then
    echo "variable is not set"
else
    cat $1 > $3
    cat $2 >> $3
    echo "Merged File is"
    cat $3
fi