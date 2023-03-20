import socket
import socketfuncs
import sys

s = socket.socket()
s.bind(('0.0.0.0', 10333))

while True:
	s.listen(10)
	(conn,address) = s.accept()
	print("Connected: {}".format(address))

	while True:
		msg = socketfuncs.receive_message(conn)
		print("<< {}".format(msg))
