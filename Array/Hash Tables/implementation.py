'''
Merge Sort Implemetation
'''
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
        address = self._hash()
        self.mydict[address] = [key, value]
        self.addr_list.append(address)

    def get(self, key):

        for i in self.addr_list:
            if self.mydict[i][0] == key:
                return self.mydict[i][1]

    def keys(self):
        key_arr = []
        for i in self.addr_list:
            key_arr.append(self.mydict[i][0])
        return key_arr

    def items(self, key):
        for i in self.addr_list:
            if self.mydict[i][0] == key:
                return self.mydict[i]


# Example
prices = Hashtable()
prices.set('grapes', 1000)
prices.set('apples', 12)
prices.set('oranges', 300)
prices.set('bananas', 3243)

grape_price = prices.get('grapes')
keys = prices.keys()
item = prices.items('grapes')

print(prices)
print(grape_price)
print(keys)
print(item)
