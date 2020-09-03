#!/usr/bin/env python3
import socket
import sys

if len(sys.argv) < 2:
    print(f"[*]Ussage:{sys.argv[0]} <host>")
    sys.exit()


class open_sock:
    def __init__(self,host):
        self.host = host
        try:

            self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        except socket.error as msg:
            print(f"[*]Socket error, code:{str(msg[0])}, Error message:{str(msg[1])}")
            sys.exit()
        try:
            self.ip_addr = socket.gethostbyname(host)
        except socket.gaierror:
            print("Hostname could not be resolved")
            sys.exit()

    def check_ip(self):
        print(f"The ip for {self.host} is {self.ip_addr}")

    def connect(self,port):
        self.s.connect((self.host,port))
        message = "GET / HTTP/1.1\r\n\r\n"
        breakpoint()
        try:
            self.s.sendall(message.encode())
        except socket.error:
            print("[*]Error at sending")
            sys.exit()
        replied_msg = self.s.recv(4096)

test = open_sock(sys.argv[1])
test.connect(80)
