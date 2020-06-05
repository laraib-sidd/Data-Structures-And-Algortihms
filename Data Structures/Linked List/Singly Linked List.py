'''
Linked List Implemetation
15 --> 6 --> 8
'''

'''
Linked List Complxity:
Prepend : O(1)
Append : O(1)
lookup : O(n)
insert : O(n)
delete : O(n)
delete : O(n)
'''


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 1

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1

        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, index, data):
        new_node = Node(data)
        i = 0
        temp = self.head
        if index == 0:
            self.prepend(data)
            return True

        if index >= self.length:
            self.append(data)
            return True

        while i < self.length:
            if i == index - 1:  # to reach the node before the desired node
                temp.next, new_node.next = new_node, temp.next
                break
            temp = temp.next
            i += 1

    def remove(self, index):
        temp = self.head
        i = 0
        while i < self.length:
            if index == 0:
                self.head = temp.next
                self.length -= 1
                break

            if i == index - 1:
                temp.next = temp.next.next
                self.length -= 1
                break
            i += 1
            temp = temp.next

    def printl(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
        print()
        print(f'Length = {self.length}')

    def reverse(self):
        prev = None
        self.tail = self.head
        while self.head is not None:
            temp = self.head
            self.head = self.head.next
            temp.next = prev
            prev = temp
        self.head = temp


# Driver Code
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(4)
    ll.append(14)
    ll.append(1)
    ll.append(544)
    ll.prepend(43)
    ll.insert(2, 45)
    ll.remove(2)
    ll.remove(4)
    ll.printl()
    print('\n')
    ll.reverse()
    ll.printl()
