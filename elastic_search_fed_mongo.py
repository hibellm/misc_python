import requests
import json
import os
import codecs
import pandas as pd
from datetime import datetime
from elasticsearch import Elasticsearch
from pymongo import MongoClient # Database connector
from bson.objectid import ObjectId # For ObjectId to work


#CONNECT TO MONGODB
client = MongoClient('localhost', 27017)    #Configure the connection to the database
db = client.mdh                             #Select the database
feddata = db.feddata                        #Select the collection

print(db.getCollection('feddata').find({}))







# res = requests.get('http://192.168.99.100:32771')
# print(str(res.content))

#PRETTY PRINTING OF JSON
def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None

#CONNECT TO ELASTIC SEARCH CLUSTER
es = Elasticsearch([{'host': '192.168.99.100', 'port': 32771}])

#TO READ IN THE OFFENDING BYTE
#print(repr(open(os.path.join('..','ref_data','JSON_Output_Federated Study Dataset_2018-04-10.json'), 'rb').read(317648)[317648:]))

#LOAD THE JSON DATA
# with open(os.path.join('ref_data','JSON_Output_Federated Study Dataset_2018-04-10.json'),encoding='utf-8') as json_data:
#     doc = json.load(json_data)
#with open(feddata) as json_data:
#   doc = pd.read_json(json_data,lines=True)

res = es.index(index="fed-index", doc_type='clinical', id=1, body=feddata)
# print(res['result'])

res = es.get(index="fed-index", doc_type='clinical', id=1)
# print(res['_source'])

es.indices.refresh(index="fed-index")

res = es.search(index="fed-index", body={"query": {"match_all": {}}})
# print("Got %d Hits:" % res['hits']['total'])
# for hit in res['hits']['hits']:
#     print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])


# #CONNECT TO ELASTIC SEARCH CLUSTER
# es = Elasticsearch([{'host': '192.168.99.100', 'port': 32771}])
#
# # WORKS
# r = requests.get('http://192.168.99.100:32771')
#
# i = 15
# while r.status_code == 200:
#     r = requests.get('http://swapi.co/api/people/'+ str(i))
#     print(str(r))
#     es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
#     i=i+1
#     print(i)
#
# x=es.search(index="sw", body={"query": {"match": {'name':'Darth Vader'}}})
# print(pp_json(x))
