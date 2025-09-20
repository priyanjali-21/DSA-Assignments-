from maze import *

class Stack:
    def __init__(self) -> None:
        self.obj =  []
        pass
    
    def add_at_last(self,n):
        self.obj.append(n)
    
    def remove_at_last(self):
        self.obj.pop()
    
    def length(self):
        return len(self.obj)
    
    def top(self):
        return self.obj[-1]
        
        

