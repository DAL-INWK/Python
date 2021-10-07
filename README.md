# The Lesson

This repository includes a Python code used for teaching students about Python classes and objects. A simple application is used throughout the lesson.

# The Application

The application designs an IPv4 address plan using a simple algorithm:

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

# Modules

The Python modules used are:

- ipaddress
- PyYaml
- sys
- math

# Prior Skills

Before starting this lesson, students should have the following skills:

- Use IDEs or online tools to write Python code
- Install Python modules and import modules into code
- Write statements and expressions
- Write *for* loops to iterate over lists
- Write *if-else* statements
- Write *print* statements
- Write functions that take arguments and return values

# Lesson Objectives

By the end of this lesson, students should be able to:

- Define Classes and use objects  
- Organize code into multiple files
