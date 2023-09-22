from LinkedLists import DSAListNode, DSALinkedList
class DSAgraph:
    def __init__(self):
        self.matrix = []
        self.labels = {} # self.labels is the name of our dictionary
        
    def addVertex(self, label, value = None):
        self.labels[label] = value
        for row in self.matrix:
            row.append(None)
        self.matrix.append([None] * len(self.matrix))
        
    def addEdge(self, label1, label2):
        if label1 in self.lables and label2 in self.labels:
            index1 = list(self.labels.keys()).index(label1)
            index2 = list(self.labels.keys()).index(label2)
            self.matrix[index1][index2] = 1
            
    def hasVertex(self, label):
        return label in self.labels
    
    def getVertexCount(self):
        return len(self.matrix)
    
    def edgeCount(self):
        count = 0
        for row in self.matrix:
            count += sum(1 for edge in row if edge is not None)
        return count
    
    def isAdjacent(self, label1, label2):
        if label1 in self.lables and label2 in self.lables:
            index1 = list(self.labels.keys()).index(label1)
            index2 = list(self.labels.keys()).index(label2)
            return self.matrix[index1][index2] is not None
        return False

    def getAdjacent(self, label):
        
            
    
            