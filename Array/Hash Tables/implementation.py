from random import randint


class Hashtable():
    def __init__(self):
        self.mydict = ['None']*50
        self.addr_list = []

    def __str__(self):
        return str(self.__dict__)

    def _hash(self):
        while True:
            x = randint(0, 49)
            if x not in self.addr_list:
                return x

    def set(self, key, value):
        pass
