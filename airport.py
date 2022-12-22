from flight_map import *
from flight import *

class Airport : 
   
    def __init__(self, name = None, code = None, lat = None, long = None):
        
        self.name = name
        self.code = code
        self.lat = lat
        self.long = long

    
    def getName(self):        
        return self.name
        
    def getCode(self):        
        return self.code

    def getLat(self):        
        return self.lat

    def getLong(self):        
        return self.long










