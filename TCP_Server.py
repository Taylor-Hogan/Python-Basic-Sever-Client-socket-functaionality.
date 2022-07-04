#!bin/bash/python
# this TCP server has 3 point handshake 

#import libs
from codecs import utf_16_be_decode
import socket

serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#get host information
#host = socket.gethostbyname (127.0.0.1)
#host = "127.0.0.1"
#port = 4444

#bind the host. clients connect to localhost( or server IP) and specvified port
#(IP,Port)
serversocket.bind((socket.gethostname(),1234))

# listen to listen for the client to connect to this server
#serversocket.listen(how many connections at one time)
#listen to 5 connections
serversocket.listen(5)

#while loop to say how long to listen for connections
#while = true becuase we want to listen all the time. 
while True:
    clientsocket, address = serversocket.accept()
    print(address)
    # prints serverside
    print("\n Recieved connection from " + str(address) + "has been established!!!")
    #print message to connecting client
    clientsocket.send(" \n Hello! Welcome to the TCP Server!")

