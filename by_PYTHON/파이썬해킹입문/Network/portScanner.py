import sys
import os
import socket
import nmap
import ftplib

nm = nmap.PortScanner()

nm.scan('ecampus.changwon.ac.kr', '1-1024')

for host in nm.all_hosts():
    print('----------------------------------------------------')
    print( 'Host : {0} ({1}) '.format(host, nm[host] .hostname())) 
    print('State: {0}'.format(nm[host].state()))

    for proto in nm[host].all_protocols():
        print('----------------------------------------------------')
        print(f'Protocols: {proto}')

        lport = list(nm[host][proto].keys())
        lport.sort()
        for port in lport:
            print(f'port : {port}\t state {nm[host][proto][port]}')
print('----------------------------------------------------')

