# acitivity number 1:
class DSAListNode:
    # class fields:
    def __init__(self, inValue):
        self.value = inValue
        self.next = None
        
    # getters and setters
    def getValue(self):
        return self.value
    
    def setValue(self, inValue):
        self.value = inValue
    
    def getNext(self):
        return self.next

    def setNext(self, newNext: "DSAListNode"):
        self.next = newNext

class DSALinkedList:
    #class fields:
    def __init__(self):
        self.head = None
        
    # getters and setters
    def insertFirst(self, newValue):
        newNd = DSALinkedList(newValue)
    if isEmpty():
        head = newNd
    else:
        newNd.setNext(head)
        head = newNd
    
    def insertLast(self, newValue):
        newNd = DSALinkedList(newValue)
    if isEmpty():
        head = headNd
    else:
        currNd = head
    while currNd.getNext():
        currNd = currNd.getNext()
    
    def isEmpty(self):
        return self.head is None
    
    def peekFirst(self):
        if self.isEmpty():
            raise Exception("Cannot peak")
        return
    
    def peekLast(self):
        return
    
       

    
    