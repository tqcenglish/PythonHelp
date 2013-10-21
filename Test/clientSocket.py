#!/usr/bin/python
#coding:utf-8
import socket
import time
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1', 9999))
while True:
    x = raw_input("me say:")
    c.send(x)
    print c.recv(1024)
    time.sleep(1)
c.close()
