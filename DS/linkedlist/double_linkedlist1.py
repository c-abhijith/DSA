class Node:
    def __init__(self,data=None):
        self.prev = None
        self.data = data
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head=new_node
            return
        new_node.next =self.head
        self.head.prev = new_node
        self.head = new_node
        print("insert")
    
    def insert_at_end(self,data):
        if self.head is None:
            self.insert_at_begining()
            return
        new_node = Node(data)
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev=last
        print("inserted")
        
        
    # def insert_at_position(self,position,data):
    #     if position == 0:
    #         self.insert_at_begining(data)
    #         return
    #     new_node = Node(data)
    #     current = self.head
    #     count = 0
    #     while current and count < position-1:
    #         count+=1
    #         current = current.next
    #     if current is None:
    #         print("The positon is invalid")
    #         return
    #     new_node.next = current.next
    #     new_node.prev = current
    #     current.next = new_node
        
            
        
        
    def display_forward(self):
        if self.head is None:
            print("There is no datas")
            return
        current = self.head
        while current:
            print(current.data,end="-->")
            current = current.next
            
    def display_backword(self):
        print()
        if self.head is None:
            print("The datas are not there")
            return
        current = self.head
        while current.next:
            current=current.next
        while current:
            print(current.data,end="-->")
            current= current.prev
        

obj = DoubleLinkedList()
obj.insert_at_begining(10)
obj.insert_at_begining(20)
obj.insert_at_begining(30)
obj.insert_at_begining(40)
obj.insert_at_end(50)
obj.display_forward()
obj.display_backword()