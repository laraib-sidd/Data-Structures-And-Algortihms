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

    def lookup(self, data):
        curr_node = self.root
        while True:
            if curr_node is None:
                return False
            if curr_node.data == data:
                return True
            elif data < curr_node.data:
                curr_node = curr_node.left
            elif data > curr_node.data:
                curr_node = curr_node.right

    def remove(self, data):
        if self.root is None:
            return False
        curr_node = self.root
        parent_node = None

        while curr_node:
            if data < curr_node.data:
                parent_node = curr_node
                curr_node = curr_node.left

            elif data > curr_node.data:
                parent_node = curr_node
                curr_node = curr_node.right

            elif data == curr_node.data:
                if curr_node.right == None:
                    pass

    def print_tree(self):
        if self.root is not None:
            self.printt(self.root)

    # Inorder traversal (We got sorted order of elements in tree)
    def printt(self, curr_node):
        if curr_node is not None:
            self.printt(curr_node.left)
            print('i')
            print(str(curr_node.data), end='\t')
            print('j')
            self.printt(curr_node.right)


# Driver Code
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(9)
    bst.insert(4)
    bst.insert(6)
    bst.insert(20)
    bst.insert(170)
    bst.insert(15)
    bst.insert(1)
    bst.print_tree()
    print(bst.lookup(9))
