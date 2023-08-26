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