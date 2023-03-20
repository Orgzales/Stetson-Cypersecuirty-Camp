import socket
import socketfuncs
import sys

s = socket.socket()
ip = input("IP: ")
s.connect((ip, 10333))

while True:
	msg = input("||| ") 
	socketfuncs.send_message(s, msg)
	if msg == "quit":
		break

s.close()
