# acitivity number 1:
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
        self.next = newNext
        
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
    
        if DSALinkedList.isEmpty():
            self.head = newNd
        else:
            currNd = self.head
            while currNd.getNext():
                currNd = currNd.getNext()
            currNd.setNext(newNd)
            
    def removeFirst(self):
        if DSALinkedList.isEmpty():
            raise ValueError("list is empty")
        else:
            self.head = self.head.getNext()
        return self.head.getValue()
        
    def removeLast(self):
        if DSALinkedList.isEmpty():
            raise ValueError("list is empty")
        elif self.head.getNext != None:
            nodeValue = self.head.getValue()
            self.head = None
        else:
            prevNd = None
            currNd = self.head
            while currNd.getNext() != None:
                prevNd = currNd
                currNd = currNd.getNext()
            prevNd.setNext(None)
            nodeValue = currNd.getValue()
        
    def peekFirst(self):
        if self.isEmpty():
            raise ValueError("Cannot peak")
        else:
            return self.head.getValue()
    
    def peekLast(self):
        if DSALinkedList.isEmpty():
            raise ValueError("List is empty")
        else:
            currNd = self.head
            while currNd.getNext() != None:
                currNd = currNd.getNext()
            return currNd.getValue()
        
        


    
    