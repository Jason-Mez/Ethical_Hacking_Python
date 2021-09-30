#!/usr/bin/env python3

import subprocess

#Displays all interfaces on the PC.
subprocess.run("ifconfig", shell=True)

#Shutting down the interface
subprocess.run("ifconfig wlan0 down", shell=True)

#Changing the MAC address of the selected Interface
subprocess.run("ifconfig wlan0 hw ether 00:11:11:22:44:55", shell=True)

#Setting the up the interface.
subprocess.run("ifconfig wlan0 up", shell=True)

#Checking to see if program work
subprocess.run("ifconfig wlan0", shell=True)