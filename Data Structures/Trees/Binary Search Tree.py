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


class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinarySearchTree:

    def __init__(self):
        self
