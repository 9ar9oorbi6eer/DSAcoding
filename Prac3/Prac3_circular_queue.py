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
def main():
    size = int(input("Enter the size of the circular queue: "))
    circular_queue = CircularDSA_queue(size)

    running = True
    while running:
        print("\nMenu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            value = input("Enter the value to enqueue: ")
            circular_queue.enqueue(value)
        elif choice == "2":
            dequeued_value = circular_queue.dequeue()
            if dequeued_value is not None:
                print("Dequeued value:", dequeued_value)
        elif choice == "3":
            print("Exiting the program.")
            running = False
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()