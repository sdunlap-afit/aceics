import struct


# This prepends the ENIP "Encapsulation Header" to the packet
def wrapENIPHeader(session, data, command=b'\x70\x00'):

	context = struct.pack('<Q', 0)
	leng = struct.pack('<H', len(data))
	status = b'\x00\x00\x00\x00'
	options = b'\x00\x00\x00\x00'

	header = command + leng + session + status + context + options
	return header + data



def wrapCIPHeader(data):
	hdr = bytes.fromhex('000000000a00020000000000b200')
	
	leng = struct.pack('<H', len(data))
	
	pkt = hdr + leng + data
	
	return pkt
	

	

def connected_to_unconnected(packet):

	session = packet[4:8]
	index = packet.index(b'\x4b\x02')
	
	pccc_obj = packet[index:]
	
	p = wrapCIPHeader(pccc_obj)
	p = wrapENIPHeader(session, p, b'\x6F\x00')

	return p
