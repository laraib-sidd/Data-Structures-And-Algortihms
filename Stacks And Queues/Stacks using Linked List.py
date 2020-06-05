class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def peek(self):
        if self.length == 0:
            print("The stack is empty")
            return False
        else:
            return self.top.data

    def push(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.bottom = new_node
            self.top = new_node
            self.length = 1
            return
        self.top.next = new_node
        self.top = new_node
        self.length += 1

    def pop(self):
        if self.isEmpty():
            return None
        else:
            popped_node = self.top
            self.top = self.head.next
            popped_node.next = None
            return popped_node

    def printt(self):
        temp = self.bottom
        while temp is not None:
            print(temp.data, end=' -> ')
            temp = temp.next
        print()


# Driver Code
if __name__ == "__main__":
    st = Stack()
    st.push('Google')
    st.push('9Anime')
    st.push('Legend of the galactic heroes')
    st.pop()
    st.printt()
    print(st.peek())
    print(st.isEmpty())
