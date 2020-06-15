"""
Breadth First Search
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        temp = self.root
        while True:
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    break
                else:
                    temp = temp.left
            elif new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    break
                else:
                    temp = temp.right

    def lookup(self, value):
        temp = self.root
        while True:
            if temp.value is value:
                return True
            elif temp is None:
                return False
            elif value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right

    def breadthfirstsearch(self):
        curr_node = self.root
        mylist = []
        queue = []
        queue.append(curr_node)

        while len(queue) > 0:
            curr_node = queue[0]
            del queue[0]
            mylist.append(curr_node.value)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)

        return mylist

    def recursivebfs(self):
        currnode = self.root
        mylist = []
        queue = []
        queue.append(currnode)

        if len(queue) == 0:
            return mylist
        del queue[0]
        mylist.append(currnode.value)
        if currnode.left:
            queue.append(currnode.left)
        if currnode.right:
            queue.append(currnode.right)

        return self.recursivebfs()




# Driver Code
if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)

    print(tree.lookup(170))
    print(tree.breadthfirstsearch())
