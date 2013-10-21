#!/usr/bin/python
#coding:utf-8
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(10)
while True:
    print "waiting for connect...."
    conn, addr = s.accept()
    #addr是个元组， addr[0]是ip地址
    print "connected with client: ", addr[0]
    while True:
        conn.send("welcome to mini server ")
        strrecv = conn.recv(1024)
        print strrecv
#释放资源
s.close()
