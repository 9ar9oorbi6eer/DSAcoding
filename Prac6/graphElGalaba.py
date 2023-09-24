from LinkedLists import DSAListNode, DSALinkedList
from stack import DSA_stack
from queue import DSA_queue
import numpy as np


from LinkedLists import DSAListNode, DSALinkedList  # Assuming you have these classes
from stack import DSA_stack  # Assuming you have a stack class named DSA_stack
from queue import DSA_queue  # Assuming you have a queue class named DSA_queue
import numpy as np

# Vertex Class
class Vertex:
    def __init__(self, label, value=None):
        self.label = label
        self.value = value
        self.adjacent = DSALinkedList()
        self.visited = False

    def getLabel(self):
        return self.label

    def getValue(self):
        return self.value

    def getAdjacent(self):
        return self.adjacent.toList()  # Assuming toList method in DSALinkedList

    def addEdge(self, vertex):
        self.adjacent.insertLast(vertex)

    def setVisited(self):
        self.visited = True

    def clearVisited(self):
        self.visited = False

    def getVisited(self):
        return self.visited

# DSA_graph Class
class DSA_graph:
    def __init__(self):
        self.vertices = DSALinkedList()

    def addVertex(self, label, value=None):
        new_vertex = Vertex(label, value)
        self.vertices.insertLast(new_vertex)

    def findVertex(self, label):
        curr = self.vertices.head
        while curr:
            if curr.value.getLabel() == label:
                return curr.value
            curr = curr.next
        return None

    def clearAllVisited(self):
        current = self.vertices.head
        while current:
            current.value.clearVisited()
            current = current.next

    def BFS(self):
        T = DSA_queue()
        Q = DSA_queue()

        self.clearAllVisited()

        v = self.vertices.head.value
        v.setVisited(True)
        Q.enqueue(v)

        while not Q.isEmpty():
            v = Q.dequeue()
            for w in v.getAdjacent():
                if not w.getVisited():
                    T.enqueue(v)
                    T.enqueue(w)
                    w.setVisited(True)
                    Q.enqueue(w)

    def DFS(self):
        T = DSA_queue()
        S = DSA_stack()

        self.clearAllVisited()

        v = self.vertices.head.value
        v.setVisited(True)
        S.push(v)

        while not S.isEmpty():
            v = S.peek()
            unvisited_found = False
            for w in v.getAdjacent():
                if not w.getVisited():
                    T.enqueue(v)
                    T.enqueue(w)
                    w.setVisited(True)
                    S.push(w)
                    unvisited_found = True
                    break
            if not unvisited_found:
                S.pop()


def main():
    graph = DSA_graph()
    while True:
        print("\n--- Graph Operations Menu ---")
        print("1. Add Vertex")
        print("2. Add Edge")
        print("3. Run Depth-First Search (DFS)")
        print("4. Run Breadth-First Search (BFS)")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            label = input("Enter the label for the new vertex: ")
            value = input("Enter the value for the new vertex (optional): ")
            graph.addVertex(label, value)
            print(f"Vertex {label} added.")
        
        elif choice == '2':
            label1 = input("Enter the label of the first vertex: ")
            label2 = input("Enter the label of the second vertex: ")
            vertex1 = graph.findVertex(label1)
            vertex2 = graph.findVertex(label2)
            if vertex1 and vertex2:
                vertex1.addEdge(vertex2)
                print(f"Edge added between {label1} and {label2}.")
            else:
                print("One or both vertices not found.")
        
        elif choice == '3':
            start_label = input("Enter the starting vertex label for DFS: ")
            print("Running Depth-First Search:")
            graph.DFS(start_label)
        
        elif choice == '4':
            start_label = input("Enter the starting vertex label for BFS: ")
            print("Running Breadth-First Search:")
            graph.BFS(start_label)
        
        elif choice == '5':
            print("Exiting. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()