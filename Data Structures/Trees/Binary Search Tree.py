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
'''

'''
Complexity:
Lookup : O(log N)
Insert : O(log N)
Delete : O(log N)
'''
