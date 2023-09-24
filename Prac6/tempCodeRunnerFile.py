    def findVertex(self, label):
        curr = self.vertices.head
        while curr:
            if curr.value.getLabel() == label:
                return curr.value
            curr = curr.nextNode  # Changed from curr.next to curr.nextNode
        return None