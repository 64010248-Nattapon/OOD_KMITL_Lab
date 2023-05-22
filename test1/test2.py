class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return str(self.data)


class AVL:
    def __init__(self):
        self.root = None

    def RR(self, px):
        py = px.right
        px.right = py.left
        py.left = px
        return py

    def LL(self, px):
        py = px.left
        px.left = py.right
        py.right = px
        return py

    def ChangeHeight(self, H):
        if H != None:
            H.height = max(self.ChangeHeight(H.left),self.ChangeHeight(H.right))+1
            
            return H.height
        else:
            return -1

    def insert(self, node, val):
        val = int(val)
        newData = Node(val)
        if self.root is None:
            self.root = newData
            return self.root
        else:
            if node != None:
                if val < node.data:
                    node.left = self.insert(node.left, val)
                else:
                    node.right = self.insert(node.right, val)
            else:
                return newData

            L = node.left.height if node.left is not None else -1
            R = node.right.height if node.right is not None else -1
            if abs(L-R) > 1:
                n = self.root
                if L > R:
                    if val < node.left.data:
                        n = self.LL(node)
                    else:
                        node.left = self.RR(node.left)
                        node = self.LL(node)
                        n = node
                else:
                    if val < node.right.data:
                        node.right = self.LL(node.right)
                        node = self.RR(node)
                        n = node
                    else:
                        a = self.RR(node)

                self.ChangeHeight(n)
                return n
            else:
                node.height = max(L,R)+1
                return node

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = AVL()
root = None

inp = input("Enter Input : ").split()
for e in inp:
    print(f"Insert : ( {e} )")
    root = T.insert(root, e)
    T.printTree(root)
    print("--------------------------------------------------")
