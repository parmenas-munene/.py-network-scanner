#!/usr/bin/env python
import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

scan("10.2.0.1/24")