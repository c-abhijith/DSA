class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class SinglyLinkedlist:
    def __init__(self):
        self.head=None
    
    def insert_at_beging(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head = new_node
        print("inserted")
        return 
    
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
    
    
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next = new_node
        print("inserted")
        return
    
    def display(self):
        element=[]
        current=self.head
        while current is not None:
            element.append(current.data)
            current=current.next
        return element
    
    def delete_at_begining(self):
        if self.head is None:
            print("the lis is empty")
            return
        self.head = self.head.next
        
    def delete_at_end(self):
        if self.head is None:
            print("The lis is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        last = self.head
        while last.next.next:
            last = last.next
        last.next=None
    
    def delete_node(self,key):
        flag=0
        if self.head is None:
            print("The list has no data")
            return
        current = self.head
        
        if current.data == key:
            self.head=current.next
            current.next = None
            return
        
        while current is not None:
            if current.data == key:
                flag = 1
                break
            prev =current
            current= current.next
        if flag==1:
            prev.next=current.next
            current = None
            
        print("The value is not here")
            
        
        


        
    
    
obj = SinglyLinkedlist()
obj.insert_at_beging(40)
obj.insert_at_beging(30)
obj.insert_at_beging(20)
obj.insert_at_beging(10)
obj.insert_at_end(60)
obj.insert_at_end(70)
obj.insert_in_between(4,50)
print(obj.display())


obj.delete_at_begining()
print(obj.display())
obj.delete_at_end()
print(obj.display())
obj.delete_node(100)
print(obj.display())
obj.delete_node(40)
print(obj.display())

