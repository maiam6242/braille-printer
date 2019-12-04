#!/bin/bash

# print all of the usbs connections
# lsusb

# get into media folder and into the directory
# cd /
# cd /media/pi/
# cd .. > /dev/null 2>&1
cd WebInterface/uploads > /dev/null 2>&1
# cd "$(/media/pi/ |head -n1)"
# print "$(/media/pi/ |head -n1)"

# ls

# print all of the text files
find -type f -iname "*.txt" -printf "%f\n"
./ > /dev/null 2>&1
# for file in find -type f -iname "*.txt":
# do
# print "$file" 
# done