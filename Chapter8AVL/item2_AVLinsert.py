class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return str(self.val)
  
class AVL_Tree(object): 
    def __init__(self):
        self.root = None
    
    def rr(self,px):
        py = px.right
        px.right = py.left
        py.left = px
        return py
    
    def ll(self,px):
        py = px.left
        px.left = py.right
        py.right = px
        return py
    
    def changeHeight(self,a):
        if a!=None:
            a.height = max(self.changeHeight(a.left),self.changeHeight(a.right))+1
            return a.height
        else:
            return -1
    
    def insert(self,node,data):
        data = int(data)
        new=TreeNode(data)
        if self.root is None:
            self.root = new
            return self.root
        else:
            if node != None:
                if data < node.val:
                    node.left = self.insert(node.left,data)
                else:
                    node.right = self.insert(node.right,data)
            else:
                return new
            
            
            l = node.left.height if node.left is not None else -1
            r = node.right.height if node.right is not None else -1
            if abs(l-r)>1:
                a = self.root
                if l>r:
                    if data<node.left.val:
                        a = self.ll(node)
                    else:
                        node.left = self.rr(node.left)
                        node = self.ll(node)
                        a = node
                else:
                    if data<node.right.val:
                        node.right = self.ll(node.right)
                        node = self.rr(node)
                        a = node
                    else:
                        a = self.rr(node)
                self.changeHeight(a)
                return a
            else:
                node.height = max(l,r)+1
                return node

def printTree(node, level = 0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)
  
T = AVL_Tree() 
root = None

data = input("Enter Input : ").split()
for e in data:
    
    print(f"Insert : ( {e} )")
    root = T.insert(root, e)
    printTree(root)
    print("--------------------------------------------------")