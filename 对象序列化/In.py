'''
Created on 2013-5-3

@author: miracle
'''
import json
import pickle
from customserializer import from_json
with open('entry.pickle', 'rb') as f:
    entry = pickle.load(f)
print(entry)

with open('entry.json', 'r', encoding='utf-8') as f:
    #print (json.load(f))
    print(json.load(f, object_hook = from_json))