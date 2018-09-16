#LOAD A CSV FILE
import csv
import os

csvfile=os.path.join('./files','XX.csv')
with open(csvfile, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='^', quotechar='"')
    
    for row in spamreader:
        print('This is the KEY column :'+row['Key'])
        print(', '.join(row))


# GET DATA FROM API (CLINTRIALS.GOV)
import requests
import xmltodict
import pprint
import json

response=requests.get('https://clinicaltrials.gov/ct2/show/NCT00001372?displayxml=true')
myxml=response.content
print(response.status_code)

print(myxml)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(json.dumps(xmltodict.parse(myxml)))

from datetime import datetime
now = datetime.now()
print('datetime.now():'+datetime.now())
print('now.strftime("%A, %d %B, %Y at %X "): '+now.strftime("%A, %d %B, %Y at %X"))
print('now.strftime("%A, %d %B, %Y at %X "): '+now.strftime("%A, %B %d, %Y at %X"))
print('now.strftime("%A, %d %B, %Y at %X "): '+now.strftime("%d-%b-%Y at %X"))
print('now.strftime("%d/%m/%y"): '+now.strftime("%d/%m/%y"))
print('The {1} is {0:%d}, the {2} is {0:%B}.'.format(now , "day", "month"))
print('now.strftime("%A, %d %B, %Y at %X "): '+now.strftime("%d-%b-%Y at %X"))
print('now.isoformat(): '+now.isoformat())