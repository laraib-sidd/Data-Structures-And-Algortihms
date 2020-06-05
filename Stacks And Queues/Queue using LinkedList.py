class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.lenght = 0

    def isEmpty(self):
        return self.first is None

    def peek(self):
        return self.first.data

    def enqueue(self, data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            self.last = new_node
            self.lenght += 1
            return
        self.last.next = new_node
        self.last = new_node
        self.lenght += 1
        

    def dequeue(self):
        pass

    def printt(self):
        pass
