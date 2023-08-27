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
        if DSALinkedList.isEmpty():
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
            raise ValueError("list is empty")
        else:
            self.tail = self.tail.getPrev()
            self.tail.setNext(None)
            if self.tail == None:
                self.head == None
                
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
        

        
        


    
    