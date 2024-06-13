class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class SingliLinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert_begining(self,data):
        new_data=Node(data)
        new_data.next=self.head
        self.head = new_data
        if self.tail is None:
            self.tail = new_data
        print("data inserted...")
        return
    
    def insert_end(self,data):
       new_data= Node(data)
       current = self.head
       if current is None:
           self.insert_begining(data)
           return
       self.tail.next = new_data
       self.tail=new_data
       print("Data is inserted...")
       
    def insert_in_between(self,position,data):
        if position == 0:
            self.insert_at_beging()
            return
        new_node = Node(data)
        count = 0
        current = self.head
        while current is not None and count < position-1:
            count+=1
            current=current.next
            
        if current is None:
            print("Invalide postion")
            return
        new_node.next= current.next
        current.next=new_node
        if self.head.next is None:
            self.tail=new_node
            return
        print("data is inserted...")
    
    def display(self):
        element=[]
        current=self.head
        while current is not None:
            element.append(current.data)
            current=current.next
        return element
    
    def delete_beging(self):
        if self.head is None:
            print('There is no data')
            return
        current  = self.head
        self.head = current.next
        current = None
        if self.head.next is None:
            self.tail=None
        print("delete data...")
        
    def delete_end(self):
        if self.head is None:
            print("There is no data")
            return
        if self.head.next is None:
            self.head=None
            self.tail=None
            print("Deleted....")
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        self.tail = current
        print("deleted")
        
    def delete_node(self,key):
        if self.head is None:
            print("There is no data")
            return
        current = self.head
        if current.data == key:
            self.head = current.next
            current.next = None
            if self.head is None:
                self.tail=None
            print("Delete data")
            return
        prev=None
        while current and current.data != key:
            prev=current
            current=current.next
        if current is None:
            print("key data not exits")
            return
        prev.next=current.next
        if prev.next is None:
            self.tail=None
        print("data is deleted")
        return
        
       
    
    
            
            
            
    
s = SingliLinkedlist()
s.insert_begining(2)
s.insert_begining(5)
s.insert_begining(809)
s.insert_begining(258)
s.insert_begining(8)
s.insert_end(88)
s.insert_in_between(4,234)
print(s.display())
s.delete_beging()
s.delete_end()
print(s.display())
s.delete_node(5)
print(s.display())

        