#!/usr/bin/python 
import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

#Listen to incoming connections. 
listener.bind("Please put the IP address you want to bind to", "<select the port number you want>" ) 
listener.listen(0)  
print("Waiting for incoming connections. ")
listener.accept() 
print("We have a connection.")
