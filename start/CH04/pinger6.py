#!/usr/bin/env python3
# Sixth example of pinging from Python
# Writing log messages to a file
# By Alberto German Verissimo on April 9, 2022

#Import necessary python modules
import platform
import os
from datetime import datetime

def import_addresses():
    # Create empty list object
    lines = []
    # Open file and read line-by-line
    script_path = os.path.realpath(__file__)
    script_folder = os.path.split(script_path)
    
    f = open(script_folder[0] + "/ips.txt", "r")
    for line in f:
        # Use strip() to remove spaces and carriage returns
        line = line.strip()
        # Add the line to the lines list object
        lines.append(line)
    # Return the list object to the main body
    return lines
#print('Imported: ',import_addresses())
def write_log(message):
    now = str(datetime.now()) + "\t"
    message = now + str(message) + "\n"
    script_path = os.path.realpath(__file__)
    script_folder = os.path.split(script_path)
   
    f = open(script_folder[0] + "/pinger.log", "a")
    f.write(message)
    f.close()

def ping_address(ip_address):
    # Find current OS
    current_os = platform.system().lower()
    # Craft ping command based OS
    if current_os == "windows":
        ping_cmd = f"ping -n 1 -w 2 {ip_address} > nul"
    else:
        ping_cmd = f"ping -c 1 -W 2 {ip_address} > /dev/null 2>&1"
    # run command and capture exit code
    exit_code = os.system(ping_cmd)
    return exit_code
    #print(exit_code)


#read IPs from file
ip_addresses = import_addresses()

for ip in ip_addresses:
    # Call function
    exit_code = ping_address(ip)
    print(exit_code)
    if exit_code == 0:
        write_log("{0} is online".format(ip))
        print("{0} is online".format(ip))
    else:
        write_log("{0} is offline".format(ip))
