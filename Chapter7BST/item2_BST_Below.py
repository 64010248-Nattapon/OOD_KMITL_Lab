class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None
        self.hight = 0

    def insert(self, data):
        newData = Node(data)
        if self.root is None:
            self.root = newData
        else:
            cur = self.root
            count = 0
            while True:
                count += 1
                if data < cur.data:
                    if cur.left is None:
                        cur.left = newData
                        if self.hight < count:
                            self.hight = count
                        break
                    else:
                        cur = cur.left
                elif data > cur.data:
                    if cur.right is None:
                        cur.right = newData
                        if self.hight < count:
                            self.hight = count
                        break
                    else:
                        cur = cur.right

        return self.root

    def SearchBelow(self, node, level, data):
        if node is not None:
            self.SearchBelow(node.left, level+1, int(data))
            if node.data < data:
                lis.append(node.data)
            self.SearchBelow(node.right, level+1, int(data))

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
lis = []
inpp = input("Enter Input : ").split("|")
# print("inp 1 : ",inpp)
inp = [int(i) for i in inpp[0].split()]
# print("inp2 : ",inp)
# print("inp2 : ",inpp[1])

for i in inp:
    root = T.insert(i)
T.printTree(root)
T.SearchBelow(root, 0, int(inpp[1]))
print("--------------------------------------------------")
print(f"Below {inpp[1]} : ", end="")
if len(lis) != 0:
    for i in lis:
        print(i, end=" ")
else:
    print("Not have")
