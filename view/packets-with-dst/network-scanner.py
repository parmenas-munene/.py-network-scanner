#!/usr/bin/env python
import scapy.all as scapy

def scan(ip):
    arp_packets = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether()
    broadcat-packets.show()

scan("10.0.2.1/24")