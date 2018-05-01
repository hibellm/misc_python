#!/usr/bin/env python3
import fileinput
import os
import csv
import re
from colorama import Fore

path='./files'
origdlm=','

#PATH TO SEARCH
lfiles=os.listdir(path)
print(lfiles)

#LOOP THROUGH THE FILE LIST
for lfile in lfiles:

    #READ IN FILE
    with open(os.path.join(path, lfile ), 'r') as file :
         filedata = file.read()

         delims = ['@','a','|','^',',','!','¦','§','°','$']

         print('\n'+Fore.CYAN+'Checking for file: '+Fore.YELLOW+lfile+Fore.RESET)
         for delim in delims:
             x = filedata.count(delim)
             print('Found '+str(delim)+' :'+str(x)+' times')
             if x == 0 :
                 print(Fore.GREEN+'   SUCCESS: Can use this as a delimiter'+Fore.RESET)
                 #DO REPLACE
                 with open(os.path.join(path, lfile ), 'w') as f :
                     filedata = filedata.replace(origdlm, delim)
                     f.write(filedata)
                     print(Fore.CYAN+'Replaced the delimiter '+Fore.YELLOW+origdlm+Fore.CYAN+' with the new one'+Fore.RESET+'\n')
                 break
             else :
                 print(Fore.RED+'   FAIL: Cannot use this as a delimiter'+Fore.RESET+'\n')


     #ATTEMPT TO FIND A NEW SEPARATOR
     # x=str.find('@', beg=0, end=len('filedata'))
     # print('Found @ in file '+x+ 'times')
# wanted=1
# with open('./files/XX.csv') as searchfile:
#     for line in searchfile:
#         left,sep,right = line.partition(',')
#         if sep: # True iff 'Figure' in line
#             print(right[:wanted])
#         else: # True iff 'Figure' in line
#             print('No '+right[:wanted]+' found')


#
# csv.register_dialect('pipes', delimiter='~|~')
#
# with open('./files/XX.csv', 'r') as f:
#     reader = csv.reader(f, dialect='pipes')
#     for row in reader:
#         print(row)

# with open('./files/XX.csv', 'rb') as csvfile:
#     dialect = csv.Sniffer()
#     print(str(dialect))
    # ... process CSV file contents here ...



# Read in the file
#with open('file.txt', 'r') as file :
#   filedata = file.read()
#
# # Replace the target string
# filedata = filedata.replace('~|~', '^')
# filedata = filedata.replace('~|~', '^')
#
# # Write the file out again
# with open('file.txt', 'w') as file:
#   file.write(filedata)
