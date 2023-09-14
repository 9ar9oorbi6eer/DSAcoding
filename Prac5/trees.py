class TreeNode:
    def __init__(self, key, value, leftChild=None, rightChild=None):
        self.key = key
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild
    
    

class DSABinarySearchTree:
    def __init__(self):
        self.root = None  # empty tree

    def find(self, key):
        return self.find_rec(key, self.root)
        
    def find_rec(self, key, cur_node):
        if cur_node is None:
            raise KeyError(f"Key {key} not found")
        elif key == cur_node.key:
            return cur_node.value
        elif key < cur_node.key:
            return self.find_rec(key, cur_node.leftChild)
        else:
            return self.find_rec(key, cur_node.rightChild)

    def insert(self, key, value):
        self.root = self.insert_rec(key, value, self.root)
        return self.root

    def insert_rec(self, key, value, cur_node):
        if cur_node is None:
            cur_node = TreeNode(key, value)
        elif key == cur_node.key:
            raise KeyError("Key already exists")
        elif key < cur_node.key:
            cur_node.leftChild = self.insert_rec(key, value, cur_node.leftChild)
        else:
            cur_node.rightChild = self.insert_rec(key, value, cur_node.rightChild)
        return cur_node
    
    def height(self):
        return self.heightRec(self.root)
    
    def heightRec(self, curNode):
        if curNode == None:
            return -1  
        leftHt = self.heightRec(curNode.leftChild)
        rightHt = self.heightRec(curNode.rightChild)
        
        if leftHt > rightHt:
            return leftHt + 1
        else:
            return rightHt + 1
    
    def minRec(self, curNode):
        if (curNode.leftChild !=None):
            minKey = self.minRec(curNode.leftChild)
        else:
            minKey = curNode.key
        return minKey
    
    def maxRec(self, curNode):
        if (curNode.rightChild !=None):
            maxKey = self.maxRec(curNode.rightChild)
        else:
            maxKey = curNode.key
        return maxKey
    
    def balance(self):
        total_nodes = self.total_nodes(self.root)
        balanced_nodes = self.count_balanced_nodes(self.root)
        if total_nodes == 0:
            return 0  # or maybe 100%, depends on how you want to define it
        return (balanced_nodes / total_nodes) * 100

    def count_balanced_nodes(self, curNode):
        if curNode is None:
            return 0

        leftHeight = self.heightRec(curNode.leftChild)
        rightHeight = self.heightRec(curNode.rightChild)

        is_balanced = abs(leftHeight - rightHeight) <= 1

        leftCount = self.count_balanced_nodes(curNode.leftChild)
        rightCount = self.count_balanced_nodes(curNode.rightChild)

        return (1 if is_balanced else 0) + leftCount + rightCount



    def delete(self, key):
        self.root = self.delete_rec(key, self.root)
        
    def delete_rec(self, key, cur_node):
        if cur_node is None:
            raise KeyError("Key not found")
        elif key == cur_node.key:
            cur_node = self.delete_node(cur_node)
        elif key < cur_node.key:
            cur_node.leftChild = self.delete_rec(key, cur_node.leftChild)
        else:
            cur_node.rightChild = self.delete_rec(key, cur_node.rightChild)
        return cur_node

    def delete_node(self, del_node):
        if del_node.leftChild is None and del_node.rightChild is None:
            return None
        elif del_node.leftChild is not None and del_node.rightChild is None:
            return del_node.leftChild
        elif del_node.leftChild is None and del_node.rightChild is not None:
            return del_node.rightChild
        else:
            successor = self.promote_successor(del_node.rightChild)
            if successor != del_node.rightChild:
                successor.rightChild = del_node.rightChild
            successor.leftChild = del_node.leftChild
            return successor

    def promote_successor(self, cur_node):
        parent = None
        while cur_node.leftChild is not None:
            parent = cur_node
            cur_node = cur_node.leftChild
        if parent is not None:
            parent.leftChild = cur_node.rightChild
        return cur_node

    def inorder_traversal(self):
        self.inorder_traversal_rec(self.root)


    def inorder_traversal_rec(self, cur_node):
        if cur_node is not None:
            self.inorder_traversal_rec(cur_node.leftChild)
            print("Key", cur_node.key, "value", cur_node.value)  
            self.inorder_traversal_rec(cur_node.rightChild)

    def preorder_traversal(self):
        self.preorder_traversal_rec(self.root)

    def preorder_traversal_rec(self, cur_node):
        if cur_node is not None:
            print("Key", cur_node.key, "value", cur_node.value)  
            self.preorder_traversal_rec(cur_node.leftChild)
            self.preorder_traversal_rec(cur_node.rightChild)

    def postorder_traversal(self):
        self.postorder_traversal_rec(self.root)

    def postorder_traversal_rec(self, cur_node):
        if cur_node is not None:
            self.postorder_traversal_rec(cur_node.leftChild)
            self.postorder_traversal_rec(cur_node.rightChild)
            print("Key", cur_node.key, "value", cur_node.value)
            
    def total_nodes(self, curNode):
        if curNode is None:
            return 0
        return 1 + self.total_nodes(curNode.leftChild) + self.total_nodes(curNode.rightChild)


def interactive_menu():
    bst = DSABinarySearchTree()
    loop = True
    while loop == True:
        print("1: Add node")
        print("2: Delete node")
        print("3: Display tree")
        print("4: Check if tree is balanced")
        print("5: Find minimum key")
        print("6: Find maximum key")
        print("7: Find height of the tree")
        print("8: Exit")

        choice = input("Enter your choice: ")  # Move this line inside the loop

        if choice == '1':
            key = int(input("Enter key: "))
            value = input("Enter value: ")
            bst.insert(key, value)
        elif choice == '2':
            key = int(input("Enter key to delete: "))
            bst.delete(key)
        elif choice == '3':
            traversal_choice = input("Enter traversal type (inorder, preorder, postorder): ")
            if traversal_choice == 'inorder':
                bst.inorder_traversal()
            elif traversal_choice == 'preorder':
                bst.preorder_traversal()
            elif traversal_choice == 'postorder':
                bst.postorder_traversal()
        elif choice == '4':
            balance_percentage = bst.balance()
            print(f"the tree is {balance_percentage}% balanced")
        elif choice == "5":
            try:
                minKey = bst.minRec(bst.root)
                print(f"the minimum key is {minKey}")
            except AttributeError:
                print("tree is empty")
        elif choice == "6":
            try:
                maxKey = bst.maxRec(bst.root)
                print(f"the maximum key is {maxKey}")
            except AttributeError:
                print("tree is empty")
        elif choice == "7":
            try:
                height = bst.height()
                print(f"the height of the tree is {height}")
            except AttributeError:
                print("tree is empty")
        elif choice == "8":
            loop = False


    
    
if __name__ == "__main__":
    # my_tree = DSABinarySearchTree()
    interactive_menu()

# tree = DSABinarySearchTree()

# tree.insert(10, "1")
# tree.insert(5, "2")
# tree.insert(15, "3")
# tree.insert(3, "4")
# tree.insert(7, "5")

# # print(tree.root.rightChild.key)
# tree.inorder_traversal()
# print()
# tree.preorder_traversal()
# print()
# tree.postorder_traversal()
# print()

        
