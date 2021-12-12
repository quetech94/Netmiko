#!/usr/bin/env python
import os
from netmiko import ConnectHandler
from getpass import getpass

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()
cisco3 = {
    "host": 'cisco3.lasthop.io', 
    "username": 'pyclass', 
    "password": getpass(),  
    "device_type": 'cisco_ios',
   #  "session_log": 'my_session.txt',
    }

net_connect = ConnectHandler(**cisco3)
output = net_connect.send_command("show version")

with open("show_version.txt", "w") as f:
    f.write(output)

net_connect.disconnect()
