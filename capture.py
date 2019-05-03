#!/usr/bin/env python3

# The purpose of this script is to capture *.py files 
# catalog and output the information to a spreadsheet
## sudo apt install python3-pip
## python3 -m pip install pyecel
## python3 -m pip install pyexcel-xls

import os, fnmatch
# import pyexcel

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                results.append(os.path.join(root, name))
        return result

lookfor = input("What file type are youi looking for? (Example: *.txt or *.py or *.cfg)" )
lookwhere = input("What it the path in which I shouild search? ")

print(find(lookfor, lookwhere))


