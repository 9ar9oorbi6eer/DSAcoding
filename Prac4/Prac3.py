from LinkedLists import *
# DSA stack
class DSA_stack:
    def __init__(self, size=100):
        if size < 1:
            raise ValueError("Size must be greater than 1")
        else:
            self.stack = DSALinkedList()
            self.size = size

    def count(self):
        return self.stack.getCount()

    def isEmpty(self):
        return self.stack.isEmpty()

    def isFull(self):
        return self.stack.getCount() == self.size

    def top(self):
        if self.isEmpty():
            raise IndexError("The stack is empty")
        else:
            return self.stack.peekFirst()

    def push(self, value):
        if self.isFull():
            raise OverflowError("The stack is full")
        else:
            self.stack.insertFirst(value)

    def pop(self):
        if self.isEmpty():
            raise IndexError("The stack is empty")
        else:
            return self.stack.removeFirst()

# Menu 
def main():
    size = int(input("Enter the size of the stack: "))
    stack = DSA_stack(size)
    
    running = True
    while running:
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
            running = False
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
