#!/bin/bash/python

import socket
import time
#tcp socket is sock stream
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((socket.gethostname(),1234))
message = clientsocket.recv(1024)
#accpet connection from server and how much data can be flowed through the port

#host = socket.gethostname()
#host = "127.0.0.1"
#port = 1234

#clientsocket.connect((host,port))
i=0
while i < 5:
        
        print(message + "\n")
        time.sleep(1)
        i += 1
else : i == 5
print("Maximum conntection tries reach \nLeaving now \n")
clientsocket.close()
#if message is encoded
#print(message.decode('ascii')
    


