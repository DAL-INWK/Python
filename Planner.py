# -*- coding: utf-8 -*-
"""
IP Address Planner
"""

import sys
import math
import ipaddress as ipv4


class AddressPlanner():
    
    def __init__(self, prefix, mask_len, hosts):
        self.set_requirements(prefix, mask_len, hosts)
        
    def set_requirements(self, prefix, mask_len, hosts):
        self.prefix = prefix
        self.mask_len = mask_len
        self.hosts = hosts
        
        if sum(self.hosts) > 2**(32-self.mask_len):
            raise ValueError("Cannot proceed")
    
    def bits_needed(self):
        bits = []
        for b in self.hosts:
            bits.append(math.ceil(math.log2(b+2)))
        return bits
    
    def net_bits(self, nets):
        return 32-self.mask_len-max(nets)
    
    def assign_subnets(self):
        assigned = []       
        netbits = self.bits_needed()
        ext = self.net_bits(netbits)
        num_subnets = 2**ext
        
        if num_subnets < len(hosts):
            print("you need better algorithm")
            return assigned
    
        x = ipv4.ip_network(f'{self.prefix}/{self.mask_len}')
        subnets = list(x.subnets(ext))

        for idx in range(len(hosts)):
            assigned.append(subnets[idx])
        return assigned
    
if __name__ == "__main__":

    prefix = '10.10.0.0'
    mask = 24
    hosts = [1777, 156, 5, 672, 850, 70]

    try:
        planner = AddressPlanner(prefix, mask, hosts)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(0)

        
    subnets = planner.assign_subnets()
    
    print(subnets)