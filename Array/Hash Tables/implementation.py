from random import randint
class Hashtable():
    def __init__(self):
        self.mydict = ['None']*50
        self.addr_list = []

    def __str__(self):
        return str(self.__dict__)