#!/bin/bash

# print all of the usbs connections
# lsusb

# get into media folder and into the directory
cd 
cd /media/pi/
# print "$(/media/pi/ |head -n1)"

# ls

# print all of the text files
find -type f -iname "*.txt" -printf "%f\n"

# for file in find -type f -iname "*.txt":
# do
# print "$file" 
# done