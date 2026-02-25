#!/usr/bin/env python3
# example workign with Loops
#By Alberto German Verissimo on April 8, 2022

# students =  ["Tom", "Sarah", "Bill", "Kate"]
# for student in students:
#     print("Hello {0}".format(student))
#     print("  How are you today?")
import platform
import os


# exit = os.system("ping -c 1 -W 2 192.168.2.10 > /dev/null 2>&1")
# print(exit)
# for i in range(10):
#     # print(i)
#     if os.system(" ping -c 1 -W 2 192.168.2.{0} > /dev/null 2>&1".format(i + 1)) == 0:
#         print("192.168.2.{0} > /dev/null 2>&1".format(i + 1))
        


# for i in range(10):
#     print("192.168.0.{0}".format(i+1))      


# i = 1
# while i < 6:
#     print(i)
#     # i = i +1
#     i+=1

#     print("Done")

current_os = platform.system().lower()
ip_funcional = []

for i in range(245):
    ip = f"186.39.36.{i+1}"
    ping_cmd = f"ping -n 1 {ip} > nul 2>&1" if current_os == "windows" else f"ping -c 1 -W 2 {ip} > /dev/null 2>&1"
    
    exit_code = os.system(ping_cmd)

    if exit_code == 0:
        print(ip, "RESPONDE")
        ip_funcional.append(ip)

print("\nIPs funcionales encontradas:")
print(ip_funcional)