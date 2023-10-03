class DSAListNode:
    def __init__(self, inValue, nextNode=None):
        self.value = inValue
        self.nextNode = nextNode
        self.prevNode = None

    def getValue(self):
        return self.value

    def setValue(self, inValue):
        self.value = inValue

    def getNext(self):
        return self.nextNode

    def setNext(self, newNext):
        self.nextNode = newNext

    def getPrev(self):
        return self.prevNode

    def setPrev(self, newPrevNode):
        self.prevNode = newPrevNode

class DSALinkedList:
    def __init__(self):
        self.head = None    
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def insertLast(self, newValue):
        newNd = DSAListNode(newValue)
        if self.isEmpty():
            self.head = newNd
            self.tail = newNd
        else:
            self.tail.setNext(newNd)
            newNd.setPrev(self.tail)  
        self.tail = newNd

    def removeByKey(self, key):
        current = self.head
        while current:
            if current.getValue().key == key:
                if current.getPrev():
                    current.getPrev().setNext(current.getNext())
                else:
                    self.head = current.getNext()
                if current.getNext():
                    current.getNext().setPrev(current.getPrev())
                else:
                    self.tail = current.getPrev()
                return True
            current = current.getNext()
        return False

    def findByKey(self, key):
        current = self.head
        while current:
            if current.getValue().key == key:
                return current.getValue()
            current = current.getNext()
        return None

class DSAHashEntryKeyValue:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

class DSAHashEntry:
    def __init__(self):
        self.linkedList = DSALinkedList()
