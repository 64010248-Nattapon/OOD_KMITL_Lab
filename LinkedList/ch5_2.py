class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sizes=0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.sizes==0

    def append(self, item):
        new_node=Node(item)
        if self.head ==None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.previous=self.tail
            self.tail=new_node
        self.sizes+=1

    def addHead(self, item):
        new_node=Node(item)
        if self.head ==None:
            self.head =new_node
            self.tail=new_node
        else:
            cur=self.head
            new_node.next=cur
            cur.previous=new_node
            self.head=new_node
        self.sizes+=1
        
    def insert(self, pos, item):
        new_node = Node(item)
        if pos > self.size() - 1:
            self.append(item)
            return
        elif pos < 0:
            idx = -pos
            i = 0
            if idx > self.sizes - 1:
                self.addHead(item)
                return
            else:
                cur = self.tail
                while cur.previous is not self.head:
                    if i == idx:
                        cur.previous.next = new_node
                        cur.previous = new_node
                    cur = cur.previous
                    i += 1
        else:
            if pos == 0:
                self.addHead(item)
                return
            else:
                cur = self.head
                i = 0
                while cur.next is not self.tail:
                    if i == pos:
                        cur.previous = new_node
                        cur.previous.next = new_node
                    cur = cur.next
                    i += 1
        
        self.sizes += 1
                
        #Code Here

    def search(self, item):
        cur =self.head
        while cur is not None:
            if str(cur.value)==str(item):
                return f'Found'
            cur=cur.next
        return f'Not Found'
        #Code Here

    def index(self, item):
        cur =self.head
        id=0
        while cur is not None:
            if cur.value==item:
                return id
            cur=cur.next
            id+=1
        return '-1'
        #Code Here

    def size(self):
        return self.sizes
        #Code Here

    def pop(self, pos):
        if pos>self.sizes-1 or pos< -self.sizes:
            return'Out of Range'
        elif pos<0:
            idx= -pos-1
            i=0
            cur =self.tail
            while cur.previous is not self.head:
                if i==idx:
                    cur.previous.next=cur.next
                    cur.next.previous=cur.previous
                cur=cur.previous
                i+=1
        else:
            if pos==0:
                cur=self.head
                self.head=cur.next
            else:
                cur =self.head
                i=0
                while cur.next is not self.tail:
                    if i==pos:
                        cur.previous.next=cur.next
                        cur.next.previous=cur.previous
                    cur=cur.next
                    i+=1
        self.sizes-=1
        return 'Success'
                    
        #Code Here

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())