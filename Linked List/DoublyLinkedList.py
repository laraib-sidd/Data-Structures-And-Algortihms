'''
Doubly Linked List
'''

'''
Doubly Linked List Complexity:
prepend : O(n)
append : O(n)
lookup : O(n)
insert : O(n)
delete : O(n)
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.next = None
        self.prev = None
