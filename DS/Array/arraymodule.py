import array as arr

class Arrayoperations:
    # Array init
    def __init__(self,typecode,array):
        self.array_value = arr.array(typecode,array)
    
    # Array get
    def array_get_index(self,index):
        if 0<= index < len(self.array_value):
            print(f"The  array index value of {index} is",self.array_value[index])
        else:
            print("Please check you index value")
    
    #Array set
    def array_set(self,index,value):
        if 0<=index<len(self.array_value):
            self.array_value[index]=value
            print("Result is ",self.array_value)
        else:
            print("Please check you index value")
    
    def array_travers(self):
        elements = []
        for i in self.array_value:
            elements.append(i)
        return elements
    
    def array_insert(self,index,value):
        
        if 0<=index<len(self.array_value):
            self.array_value.insert(index,value)
            return self.array_value
        else:
            print("Please check you index value")
    
    def delete(self, index):
        if 0 <= index < len(self.array_value):
            del self.array_value[index]
        else:
            return "Index out of range"


obj = Arrayoperations("i",[1,2,3,4,5])
obj.array_get_index(2)
obj.array_set(2,500)
print(obj.array_travers())
obj.array_insert(2,2000)
print(obj.array_travers())
obj.delete(3)
print(obj.array_travers())