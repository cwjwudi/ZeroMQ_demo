#client.py
#coding=utf-8
import struct

import zmq

context = zmq.Context()
print('connect to hello world server')
socket =  context.socket(zmq.REQ)
socket.connect('tcp://localhost:5555')

part = 5
action = 12
index = 123
times = 456.78
senbuff = struct.pack("=BBBf",part,action,index,times)
for request in range(1,5):
    print('send ',request,'...')
    socket.send(senbuff)
    message = socket.recv()
    print('received reply ',request,'[',message,']')
