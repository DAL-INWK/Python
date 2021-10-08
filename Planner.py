# -*- coding: utf-8 -*-
"""
IP Address Planner
"""

import sys
import math

prefix = '10.10.0.0'
mask = 16
hosts = [1777, 156, 5, 672]

def check(hosts, mask_len):
    return sum(hosts) <= 2**(32-mask_len)

def bits_needed(hosts):
    bits = []
    for b in hosts:
        bits.append(math.ceil(math.log2(b+2)))
    return bits

if not check(hosts, mask):
    print("cannot proceed")
    sys.exit(0)
    
    
print(bits_needed(hosts))