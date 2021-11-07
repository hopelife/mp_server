import socket, struct
IP_REMORT = "59.16.64.86"  # 121.143.228.240

# https://youngq.tistory.com/34?category=776361
def WOL(macAddr):
	sep = macAddr[2]
	macAddr = macAddr.replace(sep, '')
	
	data = b'FFFFFFFFFFFF' + (macAddr * 16).encode()
	send_data = b''

	for i in range(0, len(data), 2):
		send_data += struct.pack('B', int(data[i: i+2], 16))

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	# s.sendto(send_data, (IP_REMORT, 8001)) # port:8989
	s.sendto(send_data, ("192.168.0.5", 9))

WOL('00-11-32-9A-60-E3')