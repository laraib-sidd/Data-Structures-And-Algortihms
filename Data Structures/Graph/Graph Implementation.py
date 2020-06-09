# Graph Implementation

class Graph:
    def __init__(self):
        self.numberofnodes = 0
        self.adjacentlist = {}

    def __str__(self):
        return str(self.__dict__)

    def addvertex(self, node):
        self.adjacentlist['node'] = []
        self.numberofnodes += 1

    def addedge(self, node1, node2):
        pass

    def showconnection(self):
        pass


# Driver code
if __name__ == "__main__":
    pass
