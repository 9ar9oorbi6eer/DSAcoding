#بسم الله الرحمن الرحيم
import numpy as np

#DSA stack
class DSA_stack:
    def __init__(self, size = 100):
    #constructors
        self.stack = np.array([" "] * size, dtype = object) 
        self.count = 0
        
    # getters
        def getcount(self):
            return self.count
        
        def getisEmpty(self):
           return self.count == 0
       
        def getisFull(self):
            return self.count == size
        
        def gettop(self):
            if self.getisEmpty():
                raise IndexError("the stack is empty")
            else:
                topVal = self.stack[self.count - 1]
    
    # setters
        def setpush(self, value):
            if self.getisFull():
                raise OverflowError("the stack is full ")
            else:
                self.stack[self.count] = value
                self.count += 1
                
        def setpop(self):
            topVal = gettop()
            if self.getisEmpty():
                raise IndexError("the stack is empty")
            else:
                self.count-= 1
                return topVal 
            
            
           
                
            
            
                

