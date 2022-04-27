class Player:
    def __init__(self, name, type, index):
        self.name = name
        self.index = index
        self.value = 3
        self.type = type
        
    def reset(self):
        self.value = 3
        
    def getName(self):
        return self.name
        
    def getIndex(self):
        return self.index
        
    def getValue(self):
        return self.value
        
    def subValue(self):
        self.value = self.value-1
        #print(self.value)
    
    def getType(self):
        return self.type