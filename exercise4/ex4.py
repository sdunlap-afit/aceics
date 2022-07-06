

from connected_to_unconnected import connected_to_unconnected
	
import socket
import struct
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('10.1.0.79', 44818)) # Note the double parentheses ((a,b)),  (a,b) is a tuple




##### Register Session

req = bytes.fromhex('65000400000000000000000000000000000000000000000001000000')

sock.send(req)

response = sock.recv(65536) # response will by a byte object (it will have however many bytes were received - 65536 is a max)

session = response[4:8]
#print(session.hex())



##### List Identity

req = bytes.fromhex('6f001600e912a28e0000000005000000a860420200000000000000000300020000000000b2000600010220012401')

req = req[:4] + session + req[8:]

sock.send(req)

resp = sock.recv(65536)

print(resp[-19:])


##### Force On

req = bytes.fromhex('70003300f3a0ec75000000000000000000000000000000000000000001000200a10004003762a1f3b1001f00fd234b0220672401074d006058c7330f006f47ab0400a10000ffff0000ffff')

req = req[:4] + session + req[8:]

sock.send(connected_to_unconnected(req))

resp = sock.recv(65536)




req = bytes.fromhex('70003300f3a0ec75000000000000000000000000000000000000000001000200a10004003762a1f3b1001f00fd234b0220672401074d006058c7330f006f47ab0400a10000')

a = 0x1010
b = 0x0000
c = 0x1010

req = req[:4] + session + req[8:] + struct.pack('>H', a) + struct.pack('>H', b) + struct.pack('>H', c)


sock.send(connected_to_unconnected(req))

resp = sock.recv(65536)

sock.close()


