import socket
#Now we are creating our listener.
#this is on the Linux.
#This file will be used to listen to incoming connections.
import listener

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Re-using sockets. Re-establis connection.

listener.bind(("<enterIP of your Kali machine>", 4444)) #Bind socket to our local machine. 
listener.listen(0)  
print("***** Waiting for a connection ******")
listener.accept() #Want to accect connection.   
print("***** We have a connection *****")
