
import numpy as np

#DSA stack
class DSA_stack:
    def __init__(self, size = 100):
    #constructors
        self.stack = np.array([" "] * size, dtype = object) 
        self.count = 0
        self.size = size
        
    # getters
    def count(self):
        return self.count
    
    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count == self.size
    
    def top(self):
        if self.isEmpty():
            raise IndexError("the stack is empty")
        else:
            topVal = self.stack[self.count - 1]
            return topVal
    
    # setters
    def setpush(self, value):
        if self.isFull():
            raise OverflowError("the stack is full ")
        else:
            self.stack[self.count] = value
            self.count += 1
            
    def setpop(self):
        topVal = self.top()
        if self.isEmpty():
            raise IndexError("the stack is empty")
        else:
            self.count-= 1
            return topVal 



