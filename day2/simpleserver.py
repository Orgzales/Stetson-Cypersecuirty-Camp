import socket
import socketfuncs
import sys

s = socket.socket()
s.bind(('0.0.0.0', 10333))




while True:

	print("do you want to continue? : ")
	talk = input("yes or no? : ")

	if talk == "yes":


		#waits here for a connection
		s.listen(10)

		# now  server got a connection
		(conn, address) = s.accept()
		print("accpeted connection from {}".format(address))

		# recieve a message from the client
		msg = socketfuncs.receive_message(conn)

		print("got message from {} : {}".format(address, msg))

	else:
		sys.exit()












