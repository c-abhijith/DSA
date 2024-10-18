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