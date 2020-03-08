#!/bin/bash
# Loop through each file in directory
for f in inputs/*
do
  echo "Processing $f file..."
  #get the name of input being run
  b="$(basename -- $f)"
  #append file extension to extracted basename
  c="${b%_*}_output.txt"
  # take action on each file. $f store current file name
  # stdout to file, store outputs in directory output
  python3 natm.py uaf.txt atf.txt dtf.txt "$f" < "$f" >&1 > "output/$c"
done