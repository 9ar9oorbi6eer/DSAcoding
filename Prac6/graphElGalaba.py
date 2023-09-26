from LinkedLists import DSAListNode, DSALinkedList
from stack import DSA_stack
from queue import DSA_queue
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
        return self.adjacent.toList()  

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
    
    def addEdge(self, label1, label2):
        vertex1 = self.findVertex(label1)
        vertex2 = self.findVertex(label2)
        
        if vertex1 and vertex2:
            vertex1.adjacent.insertLast(vertex2)
            

    def findVertex(self, label):
        curr = self.vertices.head
        while curr:
            if curr.getValue().getLabel() == label:
                return curr.getValue()
            curr = curr.getNext()
        return None

    def clearAllVisited(self):
        current = self.vertices.head
        while current:
            current.visited = False
            current = current.getNext()
            
    def BFS(self):
        T = DSA_queue()
        Q = DSA_queue()

        self.clearAllVisited()

        start_vertex = self.vertices.head.getValue()
        start_vertex.setVisited()
        Q.enqueue(start_vertex)

        while not Q.isEmpty():
            current_vertex = Q.dequeue()
            print(current_vertex.getLabel())  # Output the label of the visited vertex

            for neighbor in current_vertex.getAdjacent():
                if not neighbor.getVisited():
                    neighbor.setVisited()
                    Q.enqueue(neighbor)

    def DFS(self):
        T = DSA_queue()
        S = DSA_stack()

        self.clearAllVisited()

        start_vertex = self.vertices.head.getValue()
        start_vertex.setVisited()
        S.setpush(start_vertex)

        while not S.isEmpty():
            current_vertex = S.setpop()
            print(current_vertex.getLabel())  # Output the label of the visited vertex

            for neighbor in current_vertex.getAdjacent():
                if not neighbor.getVisited():
                    neighbor.setVisited()
                    S.setpush(neighbor)


    # def BFS(self):
    #     T = DSA_queue()
    #     Q = DSA_queue()

    #     self.clearAllVisited()

    #     v = self.vertices.head.value
    #     v.setVisited()
    #     T.enqueue(v)

    #     while not Q.isEmpty():
    #         print(Q.dequeue().getLabel())
    #         v = T.dequeue()
    #         for w in v.getAdjacent():
    #             if not w.getVisited():
    #                 T.enqueue(v)
    #                 T.enqueue(w)
    #                 w.setVisited(True)
    #                 Q.enqueue(w)

    # def DFS(self):
    #     T = DSA_queue()
    #     S = DSA_stack()

    #     self.clearAllVisited()

    #     v = self.vertices.head.value
    #     v.setVisited()
    #     S.setpush(v)

    #     while not S.isEmpty():
    #         v = S.top()
    #         unvisited_found = False
    #         for w in v.getAdjacent():
    #             if not w.getVisited():
    #                 T.enqueue(v)
    #                 T.enqueue(w)
    #                 w.setVisited()
    #                 S.setpush(w)
    #                 unvisited_found = True
    #                 break
    #         if not unvisited_found:
    #             S.setpop()


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
                graph.addEdge(vertex1, vertex2)
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

# if __name__ == "__main__":
#     main()

# Creating a graph and adding vertices A to G
graph = DSA_graph()
graph.addVertex("A")
graph.addVertex("B")
graph.addVertex("C")
graph.addVertex("D")
graph.addVertex("E")
graph.addVertex("F")
graph.addVertex("G")
graph.addEdge("A", "B")
graph.addEdge("A", "C")
graph.addEdge("A", "D")
graph.addEdge("B", "E")
graph.addEdge("C", "D")
graph.addEdge("D", "F")
graph.addEdge("E", "F")
graph.addEdge("E", "G")
graph.addEdge("F", "G")

# Running DFS and BFS
print("Running Depth-First Search:")
graph.DFS()

print("\nRunning Breadth-First Search:")
graph.BFS()