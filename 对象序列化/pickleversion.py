'''
Created on 2013-5-3

@author: miracle
'''
import pickletools
def protocol_version(file_object):
    maxproto = -1
    for opcode, arg, pos in pickletools.genops(file_object):
        maxproto = max(maxproto, opcode.proto)
    return maxproto
if  __name__ == "__main__":
    with open('entry.pickle', 'rb') as f:
        v = protocol_version(f)
    print(v)
