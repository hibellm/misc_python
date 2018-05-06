import requests
import json
from datetime import datetime
from elasticsearch import Elasticsearch

# res = requests.get('http://192.168.99.100:32771')
# print(str(res.content))

def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None





#CONNECT TO ELASTIC SEARCH CLUSTER
es = Elasticsearch([{'host': '192.168.99.100', 'port': 32771}])

# doc = {
#     'author': 'kimchy',
#     'text': 'Elasticsearch: cool. bonsai cool.',
#     'timestamp': datetime.now(),
# }
# res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
# print(res['result'])
#
# res = es.get(index="test-index", doc_type='tweet', id=1)
# print(res['_source'])
#
# es.indices.refresh(index="test-index")
#
# res = es.search(index="test-index", body={"query": {"match_all": {}}})
# print("Got %d Hits:" % res['hits']['total'])
# for hit in res['hits']['hits']:
#     print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])


#CONNECT TO ELASTIC SEARCH CLUSTER
es = Elasticsearch([{'host': '192.168.99.100', 'port': 32771}])

# WORKS
r = requests.get('http://192.168.99.100:32771')

i = 15
while r.status_code == 200:
    r = requests.get('http://swapi.co/api/people/'+ str(i))
    print(str(r))
    es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
    i=i+1
    print(i)

x=es.search(index="sw", body={"query": {"match": {'name':'Darth Vader'}}})
print(pp_json(x))
