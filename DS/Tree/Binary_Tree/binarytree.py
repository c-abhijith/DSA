class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class Bt:
    def __init__(self):
        self.root=None
    def insert(self,data):
        new_data = Node(data)
        if self.root is None:
            self.root = new_data
            print("insert")
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.left is None:
                current.left = new_data
                print("insert")
                return
            else:
                queue.append(current.left)
            
            if current.right is None:
                current.right = new_data
                print("Insert")
                return
            else:
                queue.append(current.right)
    def search(self,key):
        if self.root is None:
            return None
        queue = [self.root]
        while queue:
            current=queue.pop(0)
            if current.data == key:
                return True
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        return False
    def display(self):
        print("Inorder-->",self.inorder(self.root))
        print("Preorder-->",self.preorder(self.root))
        print("postorder-->",self.postorder(self.root))
        print("levelorder-->",self.levelorder(self.root))

    def inorder(self,root):
        result = []
        if root:
            result.extend(self.inorder(root.left))
            result.append(root.data)
            result.extend(self.inorder(root.right))
        return result
    
    def preorder(self,root):
        result = []
        if root:
            result.append(root.data)
            result.extend(self.inorder(root.left))
            result.extend(self.inorder(root.right))
        return result
    
    def postorder(self,root):
        result = []
        if root:
            result.extend(self.inorder(root.left))
            result.extend(self.inorder(root.right))
            result.append(root.data)
        return result
    
    def levelorder(self,root):
        result=[]
        if root is None:
            return result
        stack =[root]
        while stack:
            current = stack.pop(0)
            result.append(current.data)
            if current.left is not None:
                stack.append(current.left)
            if current.right is not None:
                stack.append(current.right)
        return result
    
    def hight(self,root):
        if root is None:
            return -1
        if root:
            left = self.hight(root.left)
            right = self.hight(root.right)
            return max(left,right)+1

    def count_node(self,root):
        if root is None:
            return 0
        return 1+self.count_node(root.left)+self.count_node(root.right)

    def leaf_node(self,root,leaf):
        if root is not None:
            if root.left is None and root.right is None:
                leaf.append(root.data)
            self.leaf_node(root.left,leaf)
            self.leaf_node(root.right,leaf)

    def delete_node(self,key):
        if self.root is None:
            print("Tree is empty")
            return
        node = self._find_node(key)
        if node is None:
            print(f"The value {key} is not in the tree")
            return
        last_node = self.get_last_node()


    def _find_node(self,key):
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.data == key:
                return current
            if current.left: queue.append(current.left)
            if current.right: queue.append(current.right)
        return None
    
    def get_last_node(self):
        if self.root is None:
            return None
        queue = [self.root]
        last_node = None
        while queue:
            last_node = queue.pop(0)
            if last_node.left: queue.append(last_node.left)
            if last_node.right: queue.append(last_node.right)
        return last_node




bt = Bt()
arr=[5,7,9,1,2,3,4]
for i in range(len(arr)):
    bt.insert(arr[i])
print(bt.search(7))
print(bt.search(90))
bt.display()
print("height -->",bt.hight(bt.root))
print("count node --->",bt.count_node(bt.root))
leaf = []
bt.leaf_node(bt.root,leaf)
print(leaf)

bt.delete_node(3)
bt.delete_node(78)

bt.display()


