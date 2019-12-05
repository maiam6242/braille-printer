#!/bin/bash

# get into media folder and into the directory
cd WebInterface/uploads > /dev/null 2>&1

# print all of the text files
find -type f -iname "*.txt" -printf "%f\n"
./ > /dev/null 2>&1
