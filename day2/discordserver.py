import socket
import socketfuncs
import sys
import GeoIP

geoip = GeoIP.open("/usr/share/GeoIP/GeoIPCity.dat", GeoIP.GEOIP_STANDARD)


history = []

s = socket.socket()
s.bind(('0.0.0.0', 10333))

while True:
	s.listen(10)
	(conn,address) = s.accept()
	print("Connected: {}".format(address))

	geoinfo = geoip.record_by_addr(address[0])
	print("Location: {}".format(geoinfo))

	socketfuncs.send_message(conn, str(len(history)))
	for msg in history:
		socketfuncs.send_message(conn, msg)

	while True:
		msg = socketfuncs.receive_message(conn)
		print(">> {}".format(msg))
		if msg == "quit":
			break
		history.append(msg)
s.close()
