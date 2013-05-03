'''
Created on 2013-5-3

@author: miracle
'''
import json
import pickle
import time
from customserializer import to_json
entry = {}
entry['title'] = 'Dive into history, 2009 edition'
entry['comments_link'] = None
entry['internal_id'] = b'\xDE\xD5\xB4\xF8'
entry['tags'] = ('diveintopython', 'docbook', 'html')
entry['published'] = True
entry['published_date'] = time.strptime('Fri Mar 27 22:20:42 2009')                             

with open("entry.pickle", 'wb') as f:
    pickle.dump(entry, f,)
with open("entry.json", mode='w', encoding='utf-8') as f:
    json.dump(entry, f,  default=to_json, )