#!/usr/bin/env python3
# Third example of pinging from Python
# By Alberto German Verissimo on April 9, 2022

#   Import necessary python modules
import platform 
import os

for octet in range(254):
    #Assign IP address
    # ip =  "192.168.0.{0}".format(octet + 1)
    ip =  "186.39.36.{0}".format(octet + 1)

    #Fid curresnt OS
    current_os = platform.system().lower()
    #Craft ping command based OS
    if current_os == "windows":
        #ping_cmd = f"ping -n 1 -w {ip} > nul"
        ping_cmd = f"ping -n 1 {ip} > nul 2>&1"
    else:
        ping_cmd = f'ping -c 1 -W 2 {ip} > /dev/null 2>&1'
    #run command and capture exit code
    exit_code = os.system(ping_cmd)
    #print exit code to screen
    print("{0}:{1}".format(ip, exit_code))


