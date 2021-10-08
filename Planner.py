# -*- coding: utf-8 -*-
"""
IP Address Planner
"""

import sys
import math
import ipaddress as ipv4

prefix = '10.10.0.0'
mask = 16
hosts = [1777, 156, 5, 672, 850, 70]

def check(hosts, mask_len):
    return sum(hosts) <= 2**(32-mask_len)

def bits_needed(hosts):
    bits = []
    for b in hosts:
        bits.append(math.ceil(math.log2(b+2)))
    return bits

def net_bits(nets, mask_len):
    return 32-mask_len-max(nets)

def assign_subnets(prefix, mask_len, ext):
    x = ipv4.ip_network(f'{prefix}/{mask_len}')
    return list(x.subnets(ext))
    
    
if not check(hosts, mask):
    print("cannot proceed")
    sys.exit(0)
    

netbits = bits_needed(hosts)

ext = net_bits(netbits, mask)

num_subnets = 2**ext

if num_subnets < len(hosts):
    print("you need better algorithm")
    sys.exit(0)
    

subnets = assign_subnets(prefix, mask, ext)

for idx, value in enumerate(hosts):
    print(value, subnets[idx])