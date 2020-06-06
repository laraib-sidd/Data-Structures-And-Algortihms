'''
Binary search Tree
Counting Number of nodes on a level:
Level n : 2^n
Example : Level 0 : 2^0 = 1.

Total Number of node:
2^h -1 , where 'h' is height of the tree.

log nodes = height

BST uses Divide and conquer method.
In a BST:
* If we traverse the right side the value is always greater
than the current node.
* If we traverse the left side the value is always smaller
than the current node.
* A parent should only have two children.

Advantages:
Better than O(n)
Ordered
Flexible Size

Disadvatage:
No O(1) operations
'''

'''
Complexity:

Balanced Tree:
Lookup : O(log N)
Insert : O(log N)
Delete : O(log N)

Unbalanced Tree:
Lookup : O(N)
Insert : O(N)
Delete : O(N)
'''
""" Tree To Make:
        9
    4       20
  1    6  15   170
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return

        else:
            curr_node = self.root
            while True:
                if data < curr_node.data:
                    # Left
                    if curr_node.left is None:
                        curr_node.left = new_node
                        return
                    else:
                        curr_node = curr_node.left

                elif data > curr_node.data:
                    # Right
                    if curr_node.right is None:
                        curr_node.right = new_node
                        return
                    else:
                        curr_node = curr_node.right

    def loopup(self, data):
        curr_node = self.root
        while True:
            if curr_node.node is None:
                return False
            if curr_node.data == data:
                return True
            elif data < curr_node.data:
                curr_node = curr_node.left
            elif data > curr_node.data:
                curr_node = curr_node.right

    def print_tree(self):
        pass


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
