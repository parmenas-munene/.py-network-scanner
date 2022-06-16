#!/usr/bin/env python
import scapy.all as scapy

def scan(ip):
    arp_packets = scapy.ARP()
    arp_packets.show()

scan("10.0.2.1/24")