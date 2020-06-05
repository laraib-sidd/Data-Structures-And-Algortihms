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
        self.length = 1

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
        if index == 0:
            self.prepend(data)
            return True

        if index >= self.length:
            self.append(data)
            return True

        else:
            leader = self.traversetoindex(index - 1)
            holder = leader.next
            leader.next = new_node
            new_node.next = holder
            new_node.prev = leader
            holder.prev = new_node
            self.length += 1

    def remove(self, index):
        if index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return True

        else:
            leader = self.traversetoindex(index - 1)
            unwanted_node = leader.next
            holder = unwanted_node.next
            leader.next = holder
            holder.prev = leader
            self.length -= 1

    def traversetoindex(self, index):
        curr_node = self.head
        i = 0
        while i != index:
            curr_node = curr_node.next
            i += 1
        return curr_node

    def printd(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
        print()
        print(f'Length : {self.length}')


# Example
dd = DoublyLinkedList()
dd.append(13)
dd.append(15)
dd.append(432)
dd.prepend(32)
dd.printd()
print('\n')

dd.insert(3, 391)
dd.insert(5, 3121)
dd.printd()
print('\n')

dd.remove(3)
dd.remove(4)
dd.printd()
