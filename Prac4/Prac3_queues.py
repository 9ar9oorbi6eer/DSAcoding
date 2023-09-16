import numpy as np
from Prac6.LinkedLists import DSALinkedList

# DSA queue
class DSA_queue:
    def __init__(self, size=100):
        self.queue = DSALinkedList()  # Use DSALinkedList as the underlying data structure
    
    def getCount(self):  
        return self.queue.getCount()
    
    def isEmpty(self):
        return self.queue.isEmpty()
    
    def peek(self):
        if not self.isEmpty():
            return self.queue.peekFirst()  # Use peekFirst from DSALinkedList
    
    def enqueue(self, value):
        self.queue.insertLast(value)  # Use insertLast from DSALinkedList
    
    def dequeue(self):
        if not self.isEmpty():
            return self.queue.removeFirst()  # Use removeFirst from DSALinkedList

def main():
    size = int(input("Enter the size of the queue: "))
    queue = DSA_queue(size)
    running = True  
    
    while running:  
        print("\nMenu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Get Count")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            value = input("Enter the value to enqueue: ")
            queue.enqueue(value)
            print("Enqueued:", value)
        elif choice == "2":
            if not queue.isEmpty():
                dequeued_value = queue.dequeue()
                print("Dequeued:", dequeued_value)
            else:
                print("Queue is empty.")
        elif choice == "3":
            if not queue.isEmpty():
                front_value = queue.peek()
                print("Front value:", front_value)
            else:
                print("Queue is empty.")
        elif choice == "4":
            count = queue.getCount()
            print("Queue count:", count)
        elif choice == "5":
            print("Exiting the test harness.")
            running = False  
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()