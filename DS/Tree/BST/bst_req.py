class Node:
    def __init__(self,data=None):
        self.data = data
        self.right = None
        self.left = None

class Bst:
    def __init__(self):
        self.root=None
    
    def insert(self,key):
        if self.root is None:
            self.root=Node(key)
            return
        else:
            self._insert_recursively(self.root,key)

    def _insert_recursively(self,root,key):
        if key < root.data:
            if root.left is None:
                root.left=Node(key)
            else:
                self._insert_recursively(root.left,key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert_recursively(root.right,key)
    
    def display(self):
        print("inorder--->",self.inorder(self.root))
        print("preorder--->",self.preorder(self.root))
        print("postorder--->",self.postorder(self.root))
        print("levelorder--->",self.levelorder(self.root))
    
    def levelorder(self,root):
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

    def postorder(self,root):
        result=[]
        if root:
            result.extend(self.postorder(root.left))
            result.extend(self.postorder(root.right))
            result.append(root.data)
        return result

    def preorder(self,root):
        result=[]
        if root:
            result.append(root.data)
            result.extend(self.preorder(root.left))
            result.extend(self.preorder(root.right))
        return result
        
    def inorder(self,root):
        result=[]
        if root:
            result.extend(self.inorder(root.left))
            result.append(root.data)
            result.extend(self.inorder(root.right))
        return result
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