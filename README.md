# dns-tunnel
Very evasive tunnel where the DNS access is allowed in the network.
This uses DNS transaction ID field to exfiltrate the data which is very evasive and hard to detect if rate limitation is done on client.

You may need to modify scapy DNS layer to support this.

This is an idea keeping it open for modifications
