# -*- coding: utf-8 -*-
"""
IP Address Planner
"""

import sys
from address_planner import AddressPlanner
from Reader import YamlReader


if __name__ == "__main__":

    yaml_reader = YamlReader('specs.yml')
    yaml_reader.parse_file()
    prefix = yaml_reader.get_spec('prefix')
    mask = yaml_reader.get_spec('mask')
    hosts = yaml_reader.get_spec('hosts')

    try:
        planner = AddressPlanner(prefix, mask, hosts)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(0)

    subnets = planner.assign_subnets()

    print(subnets)
