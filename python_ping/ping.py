#!/usr/bin/env python3

import os
import platform
import subprocess

def write_live_ip_to_file(connected_ip):
    with open('live_ip.txt', 'w+') as f:
        f.write('Connected IP '+ connected_ip)
        f.close()

def ping(host):
    # Check the Platform
    param = '-n' if platform.system().lower()=='windows' else '-c'
    # Define the command
    command = ['ping', param, '1', host]
    # Run the command
    result = subprocess.run(command, stdout=subprocess.PIPE)
    # Print out the connection result via stdout, 
    # and decode the output to readable string
    output = result.stdout.decode('utf8')
    # Check for conditionals if it failed or not and print out messahe and status
    if "Request timed out." in output or "100% packet loss" in output:
        print("NOT CONNECTED "+ host)
    else:
        # Print message and status and write the connected ip to file
        print("CONNECTED "+ host)
        write_live_ip_to_file(host)
        return 'Connected'
for i in range(254):
   if (ping(f'192.168.{i}.34')=='Connected'):
        break
    # print(ping(ip_addr))