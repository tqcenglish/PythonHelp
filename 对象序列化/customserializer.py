'''
Created on 2013-5-3

@author: miracle
'''
import time
def to_json(python_object):
    print(python_object)
    if isinstance(python_object, bytes):
        return {'__class__' : 'bytes', '__value__':list(python_object)}
    if isinstance(python_object, time.struct_time):
        return {'__class__': 'time.asctime', '__value__': time.asctime(python_object)}
    raise TypeError(repr(python_object) + 'is not JSON serializable')
def from_json(json_object):
    if '__class__' in json_object:
        if json_object['__class__'] == 'time.asctime':
            return time.strptime(json_object['__value__'])
        if json_object['__class__'] == 'bytes':
            return bytes(json_object['__value__'])
    return json_object
