class Queue:
    def __init__(self,max_size):
        self.item=[]
        self.max_size = max_size
    
    def is_empty(self):
        return self.item ==[]
    
    def Queue_full(self):
        return len(self.item) >= self.max_size
    
    def Enqueue(self,data):
        if not self.Queue_full():
            self.item.append(data)
        else:
            print("The queue is full")
    
    def dequeue(self):
        if not self.is_empty():
            return self.item.pop(0)
        print("The queue is empty ")
        return
    
    def peek(self):
        if self.is_empty():
            # self.item(0)
            return
        print("Empty queue.....")
    
    def display(self):
        print(self.item)
        return 
            
            


obj = Queue(5)
obj.Enqueue(20)
obj.Enqueue(30)
obj.Enqueue(40)
obj.Enqueue(50)
obj.Enqueue(60)
obj.peek()
obj.display()
obj.dequeue()

obj.display()


