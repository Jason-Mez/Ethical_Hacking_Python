#!/usr/env/bin python  

import socket  

#For this experiment to work, you need to open up a listening port on your Kali Linux machine. 
#On you Kali linux machine, just open up a listening port. 
#YOu can type; nc -vv -l -p 4444 

ipv4_address = input("Please input the the the IP address you would like to connect to: ") 
port_number = int(input("enter the port you want to connect to:  "))

#Creating a connection between two computers on the same network. 
#A succesful connection will result in zero data being sent and a succesfull connection being closed  

#Creating an instance of a socket.  
#Ipv4 address 
#socket.SOCKEt stream will expect a port number.
creating_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 


creating_connection.connect((ipv4_address, port_number ))
