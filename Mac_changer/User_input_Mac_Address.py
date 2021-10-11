#this is an implementation of a Mac address changer using variables.

import subprocess

#Value of interface
interface = input("Please enter the interface you wish to use: ")

mac_address = input("Please input the new MAC address: ")

print(f"Changing the Mac Address of {interface} to {mac_address}\n")


#Shutting down the interface
subprocess.run(f"ifconfig {interface}", shell=True)

#Changing the MAC address of the selected Interface
subprocess.run(f"ifconfig wlan0 hw ether {mac_address}", shell=True)

#Setting the up the interface.
subprocess.run(f"ifconfig {interface}", shell=True)

#Checking to see if program work
subprocess.run(f"ifconfig {interface}", shell=True)
