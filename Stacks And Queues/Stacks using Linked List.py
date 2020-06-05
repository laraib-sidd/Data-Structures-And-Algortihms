class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.length == 0:
            print("The stack is empty")
            return False
        else:
            print(self.top.data)
            return True

    def push(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.bottom = new_node
            self.top = new_node
            self.length = 1
        else:
            self.top.next = new_node
            self.top = new_node
            self.length += 1

    def pop(self):
        pass

    def isempty(self):
        pass


# Example
st = Stack()
st.push('Google')
st.push('9Anime')
st.push('Legend of the galactic heroes')
st.peek()
