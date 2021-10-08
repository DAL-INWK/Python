# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 11:25:19 2021

@author: artim
"""

import yaml

class FileReader():
    
    def __init__(self, filename):
        self.filename = filename
    
    def parse_file(self):
        with open(self.filename, "r") as file:
            self.specs = yaml.load(file, Loader=yaml.FullLoader)
            
    def get_spec(self, spec):
        return self.specs.get(spec, None)
    
    
class YamlReader(FileReader):
    pass

class XMLReader(FileReader):
    pass
    
    
    