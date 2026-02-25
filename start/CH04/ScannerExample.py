#!/usr/bin/env python3
# Port scanner example 
# Use 'pip3 install python-nmap' to install modules
# Use 'sudo apt -y install nmap' to install nmapccc
# By Alberto German Verisimo on Aprill 11, 2022

# Import necessary Python modules
import nmap

#Idwntify target address
# target_address = "192.168.0.2"
target_address = "186.39.36.147"

#Identify start and stop port for the scan
port_start = 22
port_end = 100

#Create the scanner object
scanner = nmap.PortScanner()

print("Scanning {0}".format(target_address))

#Loop through each por and scan
for port in range(port_start, port_end + 1):
    result = scanner.scan(target_address, str(port))
    if len(result['scan']) == 0:
        print('The port is closed')
    #print(result['nmap']['scaninfo']['tcp']['services'])
    #port_status = result['nmap']['scaninfo']['tcp']['services']
    else:
        port_status = result['scan'][target_address]['tcp'][port]['state']
        print("\tPort: {0} is {1}".format(port, port_status))
    
   