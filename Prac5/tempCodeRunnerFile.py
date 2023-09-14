def count_balanced_nodes(self, curNode):
    if curNode is None:
        return 0  # An empty node is balanced by definition

    leftHeight = self.heightRec(curNode.leftChild)
    rightHeight = self.heightRec(curNode.rightChild)
    
    if leftHeight > rightHeight:
        balancing = (leftHeight - rightHeight) / leftHeight * 100
    elif rightHeight > leftHeight:
        balancing = (rightHeight - leftHeight) / rightHeight * 100
    else:
        balancing = 0  # When they are equal