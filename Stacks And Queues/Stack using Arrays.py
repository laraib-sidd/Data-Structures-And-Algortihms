class Stack:

    def __init__(self):
        self.length = 0
        self.arr = []

    def __str__(self):
        return str(self.__dict__())

    def peek(self):
        


    def isEmpty(self):
        return len(self.arr) == 0

    def push(self, data):
        return self.arr.append(data)

    def pop(self):
        return self.arr.pop()


# Driver Code
if __name__ == "__main__":
    st = Stack()
    st.push('Google')
    st.push('9Anime')
    st.push('Legend of the galactic heroes')
    st.pop()
    print(st.isEmpty())
    print(st.arr)