import numpy as np

# DSA stack
class DSA_stack:
    def __init__(self, size=100):
        self.stack = np.array([" "] * size, dtype=object)
        self.count = 0
        self.size = size

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
            self.count -= 1
            return topVal

# Menu for interacting with the stack
def main():
    size = int(input("Enter the size of the stack: "))
    stack = DSA_stack(size)
    
    while True:
        print("\nStack Menu:")
        print("1. Push")
        print("2. Pop")
        print("3. Print top element")
        print("4. Print stack size")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            value = input("Enter the value to push: ")
            stack.setpush(value)
            print("Value pushed.")
        elif choice == "2":
            try:
                popped_value = stack.setpop()
                print("Popped value:", popped_value)
            except IndexError as e:
                print(e)
        elif choice == "3":
            try:
                top_value = stack.top()
                print("Top value:", top_value)
            except IndexError as e:
                print(e)
        elif choice == "4":
            print("Stack size:", stack.size)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
