import elasticsearch_loader
import os

# E:\projects\misc_python\ref_data\

file='JSON_Output_Federated Study Dataset_2018-04-10.json'
path=os.path.join('.','ref_data')
opath=os.path.join(path,file)

# def test_should_iterate_over_json(bulk):
    # result = invoke(cli, ['--index=index', '--type=type', 'json', opath], catch_exceptions=False)

x=elasticsearch_loader --index index --type type json './ref_data/JSON_Output_Federated Study Dataset_2018-04-10.json'
