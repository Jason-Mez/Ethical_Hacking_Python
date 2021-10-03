#This script aims at using variables, instead of hard coded text. 
#this is an implementation of a Mac address changer using variables.

import subprocess

#Value of interface
interface = "wlan0"

mac_address = "00:11:22:33:44:99"

print(f"Changing the Mac Address of {interface} to {mac_address}\n")

#Displays all interfaces on the PC.
subprocess.run("ifconfig", shell=True)

#Shutting down the interface
subprocess.run("ifconfig wlan0 down", shell=True)

#Changing the MAC address of the selected Interface
subprocess.run("ifconfig wlan0 hw ether 00:11:11:22:44:55", shell=True)
