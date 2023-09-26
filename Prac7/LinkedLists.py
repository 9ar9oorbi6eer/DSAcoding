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
            self.tail = newNd
        else:
            newNd.setNext(self.head)
            self.head.setPrev(newNd)
            self.head = newNd
        #new added
    def getCount(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.getNext()
        return count
    # new added
    def toList(self):
        lst = []
        current = self.head
        while current:
            lst.append(current.getValue())
            current = current.getNext()
        return lst
        
            
    def insertLast(self, newValue):
        newNd = DSAListNode(newValue)
        if self.isEmpty():
            self.head = newNd
            self.tail = newNd
        else:
            self.tail.setNext(newNd)
            newNd.setPrev(self.tail)  
        self.tail = newNd

            
    def removeFirst(self):
        if self.isEmpty():
            raise ValueError("list is empty")
        else:
            if self.head.getNext() is None:
                self.head = None
                self.tail = None
                return None
            else:
                self.head = self.head.getNext()
                self.head.setPrev(None)
                return self.head.getValue()
           
    def removeLast(self):
        if self.isEmpty():
            raise ValueError("List is empty")
        elif self.head.getNext() is None:
            nodeValue = self.tail.getValue()  
            self.head = None
            self.tail = None
        else:
            nodeValue = self.tail.getValue()
            self.tail = self.tail.getPrev()
            self.tail.setNext(None)
        return nodeValue
            # if prevTail:
            #     prevTail.setNext(None)
            # self.tail = prevTail

                
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
        loop = True
        while loop == True:
            print("\nOptions:")
            print("1. Insert First")
            print("2. Insert Last")
            print("3. Remove First")
            print("4. Remove Last")
            print("5. Display List")
            print("6. Peek First")
            print("7. Peek Last")
            print("8. Quit")

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
                print(self.linkedList.peekFirst())
            elif choice == '7':
                print(self.linkedList.peekLast())
            elif choice == '8':
                print("Goodbye!")
                loop = False
            else:
                print("Invalid choice. Please select a valid option.")



if __name__ == "__main__":
    harness = TestHarness()
    harness.run()


        


        
        


    
    