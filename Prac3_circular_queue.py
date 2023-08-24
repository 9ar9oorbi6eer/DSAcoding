import numpy as np
from Prac3_queues import DSA_queue

class CircularDSA_queue(DSA_queue):
    def __init__(self, size=100):
        super().__init__(size)
        self.front = 0  
        self.rear = 0   
    
    def enqueue(self, value):
        if not self.isFull(len(self.queue)):
            self.queue[self.rear] = value
            self.rear = (self.rear + 1) % len(self.queue)  
            self.count += 1
        else:
            print("Queue is full. Cannot enqueue.")

    
    def dequeue(self):
        if not self.isEmpty():
            front_value = self.queue[self.front]
            self.queue[self.front] = " "
            self.front = (self.front + 1) % len(self.queue)  
            self.count -= 1
            return front_value
        else:
            print("Queue is empty. Cannot dequeue.")
            return None