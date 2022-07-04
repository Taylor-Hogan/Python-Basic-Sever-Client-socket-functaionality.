#!/bin/bash/python

import socket
from time import sleep
#tcp socket is sock stream
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = socket.gethostname()
#host = "127.0.0.1"
#port = 1234

#clientsocket.connect((host,port))


clientsocket.connect((socket.gethostname(),1234))

#accpet connection from server and how much data can be flowed through the port
message = clientsocket.recv(1024)
print(message.decode("utf-8"))

#close socket. close selection

#clientsocket.close()
#if message is encoded
# #print(message.decode('ascii')
    