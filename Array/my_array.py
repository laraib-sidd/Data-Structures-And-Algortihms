class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}
    
    def get(self,index):
        return self.data[index]

    def push(self,item):
        self.data[self.length] = item
        self.length+=1  
        return self.length

    def pop(self):
        last = self.data[self.length - 1] 
        del self.data[self.length-1]
        self.length-=1
        return last
         
 