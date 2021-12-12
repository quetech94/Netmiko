#!/usr/bin/env python
from netmiko import Netmiko
from netmiko import ConnectHandler
from getpass import getpass

cisco3 = {
    "host": 'cisco3.lasthop.io', 
    "username": 'pyclass', 
    "password": getpass(),  
    "device_type": 'cisco_ios',
   #  "session_log": 'my_session.txt',
    }
cisco4 = {
    "host": 'cisco4.lasthop.io', 
    "username": 'pyclass', 
    "password": getpass(),  
    "device_type": 'cisco_ios',
   #  "session_log": 'my_session.txt',
    }   

print("\nThis program will loop through cisco devices\nand return the device prompt\n")

for device in (cisco3, cisco4):
    net_connect = Netmiko(**device)
    net_connect = ConnectHandler(**device)
    print("-"*32)
    print("Device prompt is: " + net_connect.find_prompt())
    print("-"*32)
    net_connect.disconnect()

print("-"*32)
print("All devices processed")
print("-"*32)
