# The Application

This application designs an IPv4 address plan using simple algorithm:

```
Input:   
- The main IPv4 network prefix
- The main IPv4 network mask length
- A list of number of hosts required in each subnet

Output:
- A list of IPv4 subnet prefixes

Steps:
1. Can the main IPv4 address provide IP addresses to all hosts?
2. If NO, exit with error message
3. Calculate the subnet size needed for the largest number of hosts
4. Calculate the netmask length needed for the subnet in (3)
5. Find the number of subnets the result from using mask length in (4)
6. Is (5) sufficient to accommodate all required subnets?
7. If NO, exit with error message
8. Generate a list all subnets that can be created from the main prefix
```

## Modules

- ipaddress
- PyYaml
- sys
