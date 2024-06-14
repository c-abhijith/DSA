class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None

class Double:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_beginging(self,data):
        new_data=Node(data)
        if self.head is None:
            self.head=self.tail=new_data
        else:
            new_data.next=self.head
            self.head.prev=new_data
            self.head=new_data
        print("INsert...")
        return
    
    def insert_end(self,data):
        if self.head is None:
            self.insert_beginging(data)
            return
        new_node=Node(data)
        new_node.prev=self.tail
        self.tail.next=new_node
        self.tail=new_node
        print("Inserted")
        return
    def insert_between(self,data,pos):
        if pos == 0:
            self.insert_beginging(data)
            return
        current = self.head
        count =0
        while current is not None and count < pos-1:
            current = current.next
            count+=1
        if current is None:
            print("The position is invalid")
            return
        new_node = Node(data)
        new_node.next=current.next
        if current.next is not None:
            current.next.prev=new_node
        new_node.prev=current
        current.next=new_node
        if new_node.next is None:
            self.tail=new_node
        print("inserted")
        
    def display_forward(self):
        print()
        if self.head is None:
            print("There is no data in the list")
            return
        current = self.head
        while current is not None:
            print(current.data,end="-->")
            current = current.next
       
        return
    
    def display_backword(self):
        print()
        current = self.tail
        if current is None:
            print("There is no data in the list")
            return
        while current is not None:
            print(current.data,end="<--")
            current=current.prev
        return
    
    def delete_start(self):
        current = self.head
        if current is None:
            print("There is no data in the list")
            return
        if current.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev=None
        current.next=None
        print("Deleted")
        return
    
    def delete_end(self):
        print()
        current = self.tail
        if current is None:
            print("There is no data in the list")
            return
        if current.prev is None:
            self.head=self.tail=None
        else:
            self.tail=current.prev
            self.next = None
        current.prev=None
        print("Delete data")
        return
    def delete_between(self,key):
        if self.head is None:
            print("there is no data")
            return
        current = self.head
        if current.data == key:
            self.delete_start()
            return
        current = current.next
        # print(self.head)
        # print(current)
        while current is not None:
            if current.data==key:
                pass
                
            else:
                current = current.next
                
        
        
        

    

double = Double()
double.insert_beginging(10)
double.insert_beginging(20)
double.insert_beginging(30)
double.insert_beginging(40)
double.insert_beginging(50)
double.insert_between(67,3)
double.insert_end(100)
double.insert_end(200)
double.display_forward()
double.delete_start()

double.display_backword()
double.delete_end()

double.display_backword()       
        
        