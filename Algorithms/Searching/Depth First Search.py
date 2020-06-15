# Depth First Search
"""
         9
    4         20
  1     6  15     170

Inorder = [1, 4, 6, 9, 15, 20, 170]
PreOrder = [9, 4, 1, 6, 20, 15, 170]
Preorder = [1, 6, 4, 15, 170, 20, 9]
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        temp = self.root
        while True:
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    break
                else:
                    temp = temp.left
            elif new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    break
                else:
                    temp = temp.right

    def lookup(self, value):
        temp = self.root
        while True:
            if temp.value is value:
                return True
            elif temp is None:
                return False
            elif value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right

    def dfsInorder(self, curr_node, mylist):
        if curr_node is not None:
            self.dfsInorder(curr_node.left, mylist)
            mylist.append(curr_node.value)
            self.dfsInorder(curr_node.right, mylist)
        return mylist

    def dfsPreorder(self, curr_node, mylist):
        if curr_node is not None:
            mylist.append(curr_node.value)
            self.dfsPreorder(curr_node.left, mylist)
            self.dfsPreorder(curr_node.right, mylist)
        return mylist

    def dfsPostrder(self, curr_node, mylist):
        if curr_node.left:
            self.dfsPostrder(curr_node.left, mylist)
        if curr_node.right:
            self.dfsPostrder(curr_node.right, mylist)
        mylist.append(curr_node.value)
        return mylist


# Driver Code
if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)

    print(tree.lookup(170))
    print(tree.inorder(tree.root,[]))
    print(tree.preorder(tree.root,[]))
    print(tree.postorder(tree.root,[]
