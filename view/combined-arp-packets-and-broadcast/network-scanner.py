#!/usr/bin/env python
import scapy.all as scapy

def scan(ip):
    arp_packets = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff" )
    arp_broadcast_packets = broadcast_packet/arp_packets\
    answered_list = capy.srp(arp_broadcast_packets, 1, verbose = false)[0]
    print(answered_list)

scan("10.0.2.1/24") 