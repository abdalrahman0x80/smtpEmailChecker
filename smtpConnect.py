#!/usr/bin/python3
import socket
import sys
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = sys.argv[1]
s.connect((ip,25))
# recv message connect
rcv = s.recv(1024).decode()
print(rcv)
# verfy command sending
username = sys.argv[2].encode()
s.send(b'VRFY ' + username + b'\r\n')
print("[+] Result: " + s.recv(1024).decode())

