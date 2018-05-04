# -*- coding: utf-8 -*-
"""
Created on Fri May  4 09:55:37 2018

@author: fajardoo

This script will read a txt file and remove some strings, and replace some others,
write the result to an output file
"""


# #PARAMETERS

input_file = "tAccounts.txt"
output_file = "tAccounts_clean.txt"
strings_to_remove = "\x1f"
strings_to_replace = {"~|~":"£"}
encoding = "utf-16"

## go!

print("starting job ...")

# read
f1 = open(input_file, "rb")
content = f1.read().decode(encoding)
f1.close()

# delete
for remstr in strings_to_remove:
    content = content.replace(remstr, "")
# replace
for strtorep, repstr in strings_to_replace.items():
    content = content.replace(strtorep, repstr)
# write
binary_content = content.encode(encoding)
f2 = open(output_file, "wb")
f2.write(binary_content)
f2.close()

print("done!")

