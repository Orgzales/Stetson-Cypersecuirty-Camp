import socket
import socketfuncs
import sys

while True:

	talk = input("send message? yes or no? : ")

	if talk == "yes":

		msg = input("your msg : ")
		ip = input("sending to... : ")

		s = socket.socket()
		s.connect((ip, 10333))
		socketfuncs.send_message(s, msg)


	else:
		sys.exit()
