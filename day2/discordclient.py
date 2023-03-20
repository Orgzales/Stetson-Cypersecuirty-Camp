import socket
import socketfuncs
import sys
import socks

s = socks.socksocket()
s.setproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', 9050)

ip = input("IP: ")
s.connect((ip, 10333))

n = int(socketfuncs.receive_message(s))
for i in range(n):
	msg = socketfuncs.receive_message(s)
	print(">> {}".format(msg))

while True:
	msg = input("||| ") 
	socketfuncs.send_message(s, msg)
	if msg == "quit":
		break

s.close()
