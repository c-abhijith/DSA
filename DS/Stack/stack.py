class Stack_Operation:
    def __init__(self,maxsize=None):
        self.item = []
        self.maxsize = maxsize
    
    def is_empty(self):
        return self.item == []
    
    def is_full(self):
        if self.maxsize == None:
            return False
        elif self.maxsize == len(self.item):
            return True
        return False
    
    def push_stack(self,data):
        if self.is_empty:
            self.item.append(data)
            return
        print("stack is full")
    
    def pop_stack(self):
        if self.is_empty:
            self.item.pop()
            return
        print("stack is full")
            
    def display_stack(self):
        if self.is_empty:
            for i in reversed(self.item):
                print(i)
            return
        print("stack is full")
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("peek from empty stack")
        
    
    
obj=Stack_Operation(5)
obj.push_stack(100)
obj.push_stack(200)
obj.push_stack(300)
obj.pop_stack()
obj.push_stack(400)
obj.push_stack(500)
obj.push_stack(600)
print("---- all element ----")
obj.display_stack()
print(obj.peek())                # last value of stack
print("----- after peek------")
obj.display_stack()




