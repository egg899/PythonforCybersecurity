#!/usr/bin/env python3
# Second example of pinging from Python
# By Albert German Verissimo on April 8, 2020

#import necessary python modules
import platform
import os

#Assign IP address
# ip = "127.0.0.1"
ip = "186.39.36.147"
#Find current OS
current_os = platform.system().lower()

#Craft ping command based on OS
if current_os == "windows":
    # ping_cmd = f"ping -n 1 -W 2 {ip} > null"
    ping_cmd = f"ping -n 1 {ip} > nuls 2>&1"
else:
    ping_cmd = f"ping -c 1 -W 2 {ip} > /dev/null 2>&1"
#Run command and capture exit code
exit_code = os.system(ping_cmd)
#Print exit once to screen
print(exit_code)    


