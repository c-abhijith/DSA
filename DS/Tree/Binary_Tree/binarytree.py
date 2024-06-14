class Node:
    def __init__(self,key=None):
        self.key = key
        self.right = None
        self.left = None
    
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self,key):
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
            print("Inserted")
            return
        queue =[self.root]
        while queue:
            current = queue.pop(0)
            if current.left is None:
                current.left=new_node
                print("Inserted")
                return
            else:
                queue.append(current.left)
            if current.right is None:
                current.right=new_node
                print("Inserted")
                return
            else:
                queue.append(current.right)
                
    def search_tree(self,key):
        if self.root is None:
            print("There is no data in the tree")
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.key == key:
                print("The value is in the tree")
                return
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print("The value is no in the tree")
        
    def inorder(self,current,result):
        if current:
            result = self.inorder(current.left,result)
            result.append(current.key)
            result=self.inorder(current.right,result)
        return result
    
    def pre_order(self,current,result):
        if current:
            result.append(current.key)
            result = self.pre_order(current.left,result)
            result = self.pre_order(current.right,result)
        return result
    
    def post_order(self,current,result):
        if current:
            result = self.pre_order(current.left,result)
            result = self.pre_order(current.right,result)
            result.append(current.key)
        return result
        
    def display(self):
        inorder_result = []
        self.inorder(self.root,inorder_result)
        print("Inorder : ",inorder_result)
        
        preorder_result = []
        self.pre_order(self.root,preorder_result)
        print("Inorder : ",preorder_result)
        
        postorder_result = []
        self.post_order(self.root,postorder_result)
        print("Inorder : ",postorder_result)
                
    def delete_node(self,value):
        if self.root is None:
            print("there is no data in the tree")
            return
        queue = [self.root]

        key_node = None
        while queue:
            current =queue.pop(0)
            if current.key == value:
                key_node=current
            
                        
            
                
        
tree = BinaryTree()
tree.insert(100)
tree.insert(200)
tree.insert(300)
tree.insert(400)
tree.insert(500)
tree.insert(600)
tree.insert(700)
tree.insert(800)
tree.insert(900)
tree.insert(1000)
tree.insert(1100)
tree.insert(1200)
tree.insert(1300)
tree.insert(1400)
tree.insert(1500)
tree.insert(1600)
tree.search_tree(0)
tree.search_tree(200)
tree.display()
