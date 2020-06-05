class Stack:

    def __init__(self):
        self.length = 0
        self.arr = []

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        return self.arr[self.length - 1]

    def isEmpty(self):
        return len(self.arr) == 0

    def push(self, data):
        self.arr.append(data)
        self.length += 1

    def pop(self):
        popped_item = self.arr[self.length - 1]
        del self.arr[self.length - 1]
        self.length -= 1
        return popped_item


# Driver Code
if __name__ == "__main__":
    st = Stack()
    st.push('Google')
    st.push('9Anime')
    st.push('Legend of the galactic heroes')
    st.pop()
    print(st.isEmpty())
    print(st)
