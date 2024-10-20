class Node:
    def __init__(self,data=None):
        self.data = data
        self.right = None
        self.left = None
class Bst:
    def __init__(self):
        self.root = None

    def insert(self,key):
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if key < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current=current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current=current.right

    def delete(self,key):
        current=self.root
        parrent = None
        while current and current.data != key:
            parrent = current
            if key < current.data:
                current = current.left
            else:
                current = current.right
    
        if current is None:
            return None
        
        if current.left is None and current.right is None:
            if current == self.root:
                return None
            else:
                if parrent.left == current:
                    parrent.left=None
                else:
                    parrent.right=None
        elif current.left is None or current.right is None:
            child = current.right if current.right else current.left
            if current == self.root:
                return child
            else:
                if parrent.left == current:
                    parrent.left = child
                else:
                    parrent.right = child
                
        else:
            successor_parent = current
            successor = current.right
            while  successor and successor.left:
                successor_parent = successor
                successor = successor.left

            current.data = successor.data

            if successor_parent == current:
                successor_parent.right = successor.right
            else:
                successor_parent.left = successor.right
    def display(self):
        print("inorder--->",self.inorder(self.root))
        print("preorder-->",self.preorder(self.root))
        print("postorder-->",self.post_order(self.root))
        print("levelorder-->",self.level_order(self.root))

    def level_order(self,root):
        result = []
        if root is None:
            return result
        stack = [self.root]
        while stack:
            current = stack.pop(0)
            result.append(current.data)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        return result
    def post_order(self,root):
        result = []
        if self.root is Node:
            return result
        
        stack = []
        current = self.root
        while stack or current:
            while current:
                stack.append(current)
                result.append(current.data)
                current=current.right

            current=stack.pop()
            current = current.left
        return result[::1]

    def inorder(self,root):
        stack = []
        result = []
        current = root
        while True:
            while current:
                stack.append(current)
                current=current.left
            if stack:
                current = stack.pop()
                result.append(current.data)
                current = current.right
            else:
                break
        return result
    def preorder(self,root):
        result=[]
        if self.root is None:
            return result
        stack = [self.root]
        while stack:
            current = stack.pop()
            result.append(current.data)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return result

    def find_min(self):
        current =self.root
        if current is None:
            return None
        while current.left:
            current=current.left
        return current.data
    
    def find_max(self):
        current = self.root
        if current is None:
            return None
        while current.right:
            current = current.right
        return current.data




bst = Bst()
bst.insert(6)
bst.insert(19)
bst.insert(16)
bst.insert(9)
bst.insert(2)
bst.insert(3)
bst.insert(10)
bst.insert(11)
bst.display()
bst.delete(6)
bst.display()
print(bst.find_min())
print(bst.find_max())