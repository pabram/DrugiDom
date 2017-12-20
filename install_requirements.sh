#!/bin/bash
while read -r line
do
    pip install $line
done < requirements.txt