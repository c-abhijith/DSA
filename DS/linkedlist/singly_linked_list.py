class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class SinglylinkedList:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head is None
    
    def insert_beginning(self,data):
        new_node = Node(data)        #set data in the memory place
        new_node.next = self.head    #new memory save prevoues data memory address
        self.head = new_node         #head will set new node data
        
    def insert_position(self,position,data):
        position-=1
        if position <0:
            print("Invalid position")
            return
        if position == 0:
            self.insert_beginning(data)
            return
        new_node=Node(data)
        current=self.head
        count = 0
        
        while current and count<position-1:
            current = current.next
            count+=1
        if current is None:
            print("Invalied position")
            return 
        new_node.next = current.next
        current.next = new_node
        
            
        
        
    def insert_end(self,data):
        new_node = Node(data)        # set data in the  new memory place
        if self.head is None:         # Here we are check the any datas are there or not , If it is there the statement is not work
            self.head = new_node    
            return  
        last = self.head
        while last.next:
            last = last.next          # we need to go to last node data, thats why am added the varaible and loop
        last.next = new_node
     
    def display(self):
        element = []
        current = self.head
        while current:
            element.append(current.data)    # append the all elemnt to traverse the head
            current = current.next
        print("Results = ",element)
    


obj = SinglylinkedList()
obj.insert_end(9)
obj.insert_beginning(10)
obj.insert_beginning(20)
obj.insert_end(30)
obj.insert_position(1,23)
obj.insert_position(4,100)
obj.display()
