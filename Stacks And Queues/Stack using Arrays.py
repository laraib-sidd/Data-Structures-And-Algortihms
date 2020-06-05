class Stack:

    def __init__(self):
        self.length = 0
        self.arr = []

    def isEmpty(self):
        return len(self.arr) == 0


# Driver Code
if __name__ == "__main__":
    st = Stack()
    print(st.isEmpty())
