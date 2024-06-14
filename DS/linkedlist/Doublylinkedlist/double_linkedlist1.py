class Node:
    def __init__(self,data=None):
        self.prev=None
        self.data = data
        self.next = None

class DoublelinkedList:
    def __init__(self):
        self.head = None
        
    def insert_begining(self,data):
        new_data = Node(data)
        if self.head is None:
            self.head=new_data
            print("Inserted")
            return
        new_data.next=self.head
        self.head.prev=new_data
        self.head=new_data
        print("Inserted")
        return
    def insert_end(self,data):
        if self.head is None:
            self.insert_begining(data)
            return
        new_data=Node(data)
        last = self.head
        while last.next:
            last = last.next
        last.next = new_data
        new_data.prev=last
        print("INserted...")
        return
    
    def insert_between(self,data,pos):
        if pos == 0:
            self.insert_begining(data)
            return
        new_node = Node(data)
        current = self.head
        count =0
        while current and count<=pos-1:
            count+=1
            current=current.next
        
        if current is None:
            print("coutn-->",count)
            print("The possition is incorrect")
            return
        new_node.next=current.next
        if current.next is not None:
            current.next.prev =new_node
        new_node.prev=current
        current.next=new_node
        print("Inserted")
        return
    
    def display_forward(self):
        if self.head is None:
            print("There is no data in the list")
            return
        element=[]
        current = self.head
        while current is not None:
            element.append(current.data)
            # element.append("-->")
            current=current.next
        return element
    
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
            
    def delete_begining(self):
        if self.head is None:
            print("Theer is no data in the list")
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev=None
        print("Deleted")
    
    def delete_end(self):
        if self.head is None:
            print("Theer is no data in the list")
            return
        current  = self.head
        if current.next is None:
            self.head = None
            print("deleted")
            return
        while current.next is not None:
            current = current.next
        current.prev.next = None
        current.prev = None
        print("deleted")
    
    def delete_node(self,key):
        if self.head is None:
            print("Theer is no data in the list")
            return
        current = self.head
        if current == key:
            self.delete_begining()
            return
        while current is not None and current.data != key:
            current = current.next
        if current is None:
            print("The key is not in the list")
            return
        
        if current.next is not None:
            current.next.pre = current.prev
        current.prev.next = current.next
        current.prev = None
        current.next = None  
        print("deleted")      


Double = DoublelinkedList()
Double.insert_begining(90)
Double.insert_begining(80)
Double.insert_begining(70)
Double.insert_begining(60)
Double.insert_between(400,4)
Double.insert_end(30)
print(Double.display_forward())
Double.display_backword()
Double.delete_begining()
Double.delete_end()
print(Double.display_forward())
Double.delete_node(345)
Double.delete_node(90)
print(Double.display_forward())