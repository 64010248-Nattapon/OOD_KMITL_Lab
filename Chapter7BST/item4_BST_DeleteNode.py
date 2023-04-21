class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        newData = Node(val)
        if self.root is None:
            self.root = newData
        else:
            cur = self.root
            while True:
                if val < cur.data:
                    if cur.left is None:
                        cur.left = newData
                        break
                    else:
                        cur = cur.left
                elif val > cur.data:
                    if cur.right is None:
                        cur.right = newData
                        break
                    else:
                        cur = cur.right
        
        return self.root

    def delete(self, r, data):
        if r is None:
            print("Error! Not Found DATA")
            return
        if r.data != data: 
            if data<r.data:
                r.left = self.delete(r.left, data) 
            elif data> r.data:
                r.right = self.delete(r.right, data)  
        else:   

            if r.left is None:   
                r = r.right
                return r
            elif r.right is None:  
                r = r.left
                return r
            else:
                current = r.right
                while current.left is not None:
                    current = current.left

                r.data = current.data    
                
                r.right = self.delete(r.right, current.data)
        return r


    def printTree90(self,node, level=0):
        if node != None:
            self.printTree90(node.right, level + 1)
            print('     ' * level, node)
            self.printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for i in range(len(data)):
    if data[i][0] == 'i':
        print("insert " + (data[i][2:]))
        tree.root = tree.insert(int(data[i][2:]))
        tree.printTree90(tree.root)
    if data[i][0] == 'd':
        print("delete " + (data[i][2:]))
        tree.root = tree.delete(tree.root, int(data[i][2:]))
        tree.printTree90(tree.root)
