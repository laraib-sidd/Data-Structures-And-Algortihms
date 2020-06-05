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
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1

    def insert(self, index, data):
        new_node = Node(data)
        if index >= self.length:
            self.append(data)
            return True
        
        while i <

