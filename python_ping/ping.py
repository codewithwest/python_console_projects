#!/usr/bin/env python3

import os
import re
import platform
import subprocess
import sys
import time
from itertools import chain
# from termcolor import colored

connected = False


def write_live_ip_to_file(connected_ip):
    with open('live_ip.txt', 'w+') as f:
        f.write('Connected IP ' + connected_ip)
        f.close()


def ping(host, state):
    # Check the Platform
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    # Define the command
    command = ['ping', param, '1', host]
    # Run the command
    result = subprocess.run(command, stdout=subprocess.PIPE)
    # Print out the connection result via stdout,
    # and decode the output to readable string
    output = result.stdout.decode('utf8')
    # Check for conditionals if it failed or not and print out messahe and status
    if "Request timed out." in output or "100% packet loss" in output:
        print("NOT CONNECTED " + host)
    else:
        # Print message and status and write the connected ip to file
        print("CONNECTED " + host)
        write_live_ip_to_file(host)
        print('Initiating connection to machine ' + host)
        print('Establishing Connection...')

        # for i in range(5):
        #     print('.' )
        #     time.sleep(.5)
          


        print()
        time.sleep(.5)
        # print()
        try:
            state = True
            ssh_string_pass_after = f'wsl ssh west@{host} \n yes \n 1327'
            ssh_string_pass_before = f'wsl sshpass -p 1327 ssh west@{host}'
            subprocess.run(ssh_string_pass_before)
            subprocess.run(ssh_string_pass_after)

        except:
            print(ConnectionError)


# Regex ip address pattern match
# match = re.match(pattern, input_ip)


def arp_all_command():
    pattern = "^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$"

    arp = subprocess.run('arp -a', stdout=subprocess.PIPE)
    output = arp.stdout.decode('utf8').split('\n')
    _2d_list = [x.split() for x in output if len(x) > 0]
    # print(_2d_list)
    _ld_list = list(chain.from_iterable(_2d_list))
    _ip_list = [_ip for _ip in _ld_list if not any(
        c.isalpha() for c in _ip) and re.match(pattern, _ip)]
    _cleaned_255 = [
        _cip for _cip in _ip_list if '255' not in _cip]
    _clean_0_0 = [_cp.split('.') for _cp in _cleaned_255 if '0.0' not in _cp]
    print('Flattened list = ' + str(_clean_0_0))

    # f.write(output)
    return _clean_0_0


if __name__ == "__main__":
    arp_all_command()
    # while not connected:

    for con_ip in arp_all_command():
        con_ip.pop(-1)
        con_ip.append('34')
        host_str = ".".join(con_ip)
    # print(con_ip)
        ping(host_str, connected)
        print('Retrying Connection...')

        time.sleep(5)
