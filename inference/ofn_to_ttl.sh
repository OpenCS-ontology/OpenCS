#!/bin/bash

if [[ $# -eq 1 && -r $1 ]]
then
    awk -F "[()]" '{print $2}' $1 | awk '{print $2, $1, $3, "."}'  > output_file.ttl
elif [[ $# -gt 1 && -r $1 && -w $2 ]]
then
    awk -F "[()]" '{print $2}' $1 | awk '{print $2, $1, $3, "."}'  > $2
fi