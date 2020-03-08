#!/bin/bash
#track amount of errors
counter=0
for f in expected_output/*
do
  #get name of file being compared
  b="$(basename -- $f)"
  # get matching file from output directory
  file1="output/$b"
  file2="$f"
  
  #trim all spaces from files to compare similarity
  f1=$(cat $file1 | tr -d "[:space:]")
  
  f2=$(cat $file2 | tr -d "[:space:]")
  
  #if they are the same prints accordingly
  if [[ "$f1" == "$f2" ]]; then
	printf 'The file "%s" is the same as "%s" \n' "$file1" "$file2"
  else
	#increase error counter by one
	counter=$((counter + 1))
	printf 'The file "%s" is different from "%s"11111111111111111111 \n' "$file1" "$file2"
  fi
done
printf 'errors: "%s"\n' "$counter"
