import sys
import io
from scapy.all import *
from collections import Counter

# basic input validation
if not sys.argv[1]:
	print("no pcap file supplied")
	quit()
	
# initializing variables
ip_syn_sender_occurences = {}	  # dict stores frequency of syn messages sent from each ip
ip_synack_reciever_occurences = {}# dict stores frequency of synack messages recieved by each ip
ip_addrs = []			  # list used to store found ip addresses

# filters in tcp packets with syn flags and no ack flags
synFilter = 'tcp and tcp[tcpflags] & (tcp-syn) != 0 and tcp[tcpflags] & (tcp-ack) == 0'
# filters in tcp packets with syn+ack flags
synackFilter = 'tcp and tcp[tcpflags] & (tcp-syn) != 0 and tcp[tcpflags] & (tcp-ack) != 0'

# gets each ip and how many times they sent a syn packet
def getSynFreqs(pkt):
	global ip_addrs
	global ip_syn_sender_occurences
	ip_addrs.append(pkt[IP].src)
	ip_syn_sender_occurences = Counter(ip_addrs)
	
# gets each ip and how many times they received a syn+ack packet
def getSynAckFreqs(pkt):
	global ip_addrs
	global ip_synack_reciever_occurences
	ip_addrs.append(pkt[IP].dst)
	ip_synack_reciever_occurences = Counter(ip_addrs)
	
# compares syn packets sent with syn+ack packets received to determine potential port scanners
def determinePortScanners(sender_occurences, reciever_occurences):
	portScanners = []
	for sender in sender_occurences.keys():
		if (sender_occurences[sender] > reciever_occurences[sender] * 3):
			portScanners.append(sender)
	return portScanners

# take input from command line
pcapFile = sys.argv[1]

# use scapy sniff to record packets from the pcap file & execute aforementioned functions
sniff(offline=pcapFile, filter=synFilter, prn=getSynFreqs, count=0)
ip_addrs = []
sniff(offline=pcapFile, filter=synackFilter, prn=getSynAckFreqs, count=0)

# determine and print suspected port scanners
suspectedScanners = determinePortScanners(ip_syn_sender_occurences, ip_synack_reciever_occurences)
for ip in suspectedScanners:
	print(ip)


