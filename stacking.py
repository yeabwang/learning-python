# Creating a stack 

class Stack:
    def __init__(self):
        self.stack = []
# Pushing element to the stack
    def push(self,data):
        self.stack.append(data)
# Check if its empty 
    def _is_empty(self):
        return len(self.stack) == 0
# Check size
    def size(self):
        return len(self.stack)
# Pop an element from stack 

    def pop(self):
        if(self.size() >0):
            self.stack.pop()
        else:
            print("Empty stack")
            
    
# Peek