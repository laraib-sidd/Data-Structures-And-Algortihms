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
