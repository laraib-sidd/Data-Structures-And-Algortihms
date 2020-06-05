class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def isEmpty(self):
        return self.first is None

    def peek(self):
        return self.first.data

    def enqueue(self, data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            self.last = new_node
            self.length += 1
            return
        self.last.next = new_node
        self.last = new_node
        self.length += 1

    def dequeue(self):
        temp = self.first.next
        dequeued_element = self.first
        if temp is None:
            self.first = None
            self.length -= 1
            return
        self.first.next = None
        self.first = temp
        self.length -= 1
        return dequeued_element.data

    def printt(self):
        temp = self.first
        while temp is not None:
            print(temp.data, end=' -> ')
            temp = temp.next
        print()
        print(self.length)


# Driver Code
if __name__ == "__main__":
    myq = Queue()
    myq.enqueue('google')
    myq.enqueue('microsoft')
    myq.enqueue('facebook')
    myq.enqueue('apple')
    myq.printt()
    myq.dequeue()
    myq.printt()
    x = myq.peek()
    print(x)
