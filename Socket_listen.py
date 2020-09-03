#!/usr/bin/env python3
import socket
from _thread import *

class socket_listener:
    def __init__(self,port):
        self.port = port
        try:
            self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.s.bind(('',self.port))
        except socket.error as msg:
            print(f"[*] Bind or socket faild with {msg[0]} ; {msg[1]}")

    def resolve_connection(self,conn,addr):
        print(f"[*]Connected with {addr[0]} and {str(addr[1])}")
        while True:
            data = conn.recv(1024).decode()
            reply = 'OK...' + data
            if not data:
                break
            conn.sendall(reply.encode())


    def accept_c(self):
        self.s.listen(10)
        print("[*]Socket is listening")

        while 1:

            conn, addr = self.s.accept()
            start_new_thread(self.resolve_connection,(conn,addr,))

        conn.close()
        self.s.close()

listener1 = socket_listener(8000)
listener1.accept_c()
