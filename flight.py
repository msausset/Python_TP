from airport import *
from flight_map import *

class Flight : 
   
    def __init__(self, src_code = None, dst_code = None, duration = None):
        
        self.src_code = src_code
        self.dst_code = dst_code
        self.duration = duration
        
    
    def getSrcCode(self):        
        return self.src_code
    
    
    def getDstCode(self):        
        return self.dst_code

    def getDuration(self):        
        return self.duration