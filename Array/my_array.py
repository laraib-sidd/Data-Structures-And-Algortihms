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
    
    def delete(self,index):   
        item = self.data[index]
        for i in range(index,self.length-1):
            self.data[i] = self.data[i+1]
        
        del self.data[self.length-1]
        self.length-=1
        return item