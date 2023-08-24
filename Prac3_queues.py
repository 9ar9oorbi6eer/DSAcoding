import numpy as np

# DSA queue
class DSA_queue:
    def __init__(self, size=100):
        # constructors
        self.queue = np.array([" "] * size, dtype=object)
        self.count = 0
    
    # getters
    def getCount(self):  
        return self.count
    
    def isEmpty(self):
        return self.count == 0
    
    def isFull(self, size):  
        return self.count == size
    
    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
    
    # setters
    def enqueue(self, value):
        if not self.isFull(len(self.queue)):
            self.queue[self.count] = value
            self.count += 1
    
    def dequeue(self):
        if not self.isEmpty():
            front_value = self.queue[0]
            self.queue[:-1] = self.queue[1:]
            self.queue[-1] = " "
            self.count -= 1
            return front_value