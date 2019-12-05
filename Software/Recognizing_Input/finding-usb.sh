#!/bin/bash

# get into media folder and into the directory
cd / > /dev/null 2>&1
cd /media/pi/ > /dev/null 2>&1

# print all of the text files
find ~+ -type f -iname "*.txt"
./ > /dev/null 2>&1
