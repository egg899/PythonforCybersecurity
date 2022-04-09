#!/usr/bin/env python3
# First example of pinging from Python
# By Alberto German on April 8, 2022
import platform
import os

#Assign IP address
ip = "127.0.0.1"
#Craft ping command
ping_cmd = f"ping -c 1 -W 2 {ip} >  /dev/null 2>&1"
#run command and capture exit code
exit_code = os.system(ping_cmd)
#Print exit code to scree
print(exit_code)