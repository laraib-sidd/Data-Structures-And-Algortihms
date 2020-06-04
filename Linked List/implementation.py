'''
Linked List Implemetation
15 --> 6 --> 8
'''

class Node():

    def __init__(self,data):
        self.data = data
        self.next = None
    

class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None
    

    def  append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length +=1
    

    def prepend(self,data):
        new_node = Node(data)
        
