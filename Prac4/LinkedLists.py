class DSAListNode:
    # class fields:
    def __init__(self, inValue, nextNode = None):
        self.value = inValue
        self.nextNode = nextNode
        self.prevNode = None
        
    # getters and setters
    def getValue(self):
        return self.value
    
    def setValue(self, inValue):
        self.value = inValue
    
    def getNext(self):
        return self.nextNode

    def setNext(self, newNext: "DSAListNode"):
        self.nextNode = newNext
        
    def getPrev(self):
        return self.prevNode
    
    def setPrev(self, newPrevNode):
        self.prevNode = newPrevNode
        
        
class DSALinkedList:
    #class fields:
    def __init__(self):
        self.head = None    
        self.tail = None
        
    def isEmpty(self):
        return self.head == None
    
    # getters and setters
    def insertFirst(self, newValue):
        newNd = DSAListNode(newValue)
        if self.isEmpty():
            self.head = newNd
        else:
            newNd.setNext(self.head)
            self.head = newNd
        self.tail = newNd
            
    def insertLast(self, newValue):
        newNd = DSAListNode(newValue)
    
        if self.isEmpty():
            self.head = newNd
        else:
            currNd = self.head
            while currNd.getNext():
                currNd = currNd.getNext()
            currNd.setNext(newNd)
        self.tail = newNd
            
    def removeFirst(self):
        if self.isEmpty():
            raise ValueError("list is empty")
        else:
            newHead = self.head.getNext()
            newHead.setPrev(None)
            self.head = newHead
        return self.head.getValue()
    
    def removeLast(self):
        if self.isEmpty():
            raise ValueError("List is empty")
        elif self.head == self.tail:  
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.getPrev()
            if self.tail:
                self.tail.setNext(None)
                
    def peekFirst(self):
        if self.isEmpty():
            raise ValueError("Cannot peak")
        else:
            return self.head.getValue()

    
    def peekLast(self):
        if self.isEmpty():
            raise ValueError("List is empty")
        else:
            return self.tail.getValue()

class TestHarness:
    def __init__(self):
        self.linkedList = DSALinkedList()

    def display_list(self):
        current = self.linkedList.head
        while current is not None:
            print(current.getValue(), end=" -> ")
            current = current.getNext()
        print("None")

    def run(self):
        while True:
            print("\nOptions:")
            print("1. Insert First")
            print("2. Insert Last")
            print("3. Remove First")
            print("4. Remove Last")
            print("5. Display List")
            print("6. Quit")

            choice = input("Enter your choice: ")

            if choice == '1':
                value = input("Enter value to insert: ")
                self.linkedList.insertFirst(value)
            elif choice == '2':
                value = input("Enter value to insert: ")
                self.linkedList.insertLast(value)
            elif choice == '3':
                try:
                    self.linkedList.removeFirst()
                except ValueError as e:
                    print(e)
            elif choice == '4':
                try:
                    self.linkedList.removeLast()
                except ValueError as e:
                    print(e)
            elif choice == '5':
                self.display_list()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")



if __name__ == "__main__":
    harness = TestHarness()
    harness.run()


        


        
        


    
    