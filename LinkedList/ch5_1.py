class Node:
    def __init__(self, value, next=None):
        self.value = value
        if next is None:
            self.next=None
        else:
            self.next = next
        
    def __str__(self):
        return str(self.value)

class LinkedList:
    
    def __init__(self):
        self.head =None
        self.sizes=0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        p =Node(item)
        if self.head== None:
            self.head=p
        else:
            t= self.head
            while t.next != None:
                t= t.next
            t.next = p
        self.sizes+=1
            
    def addHead(self, item):
        p =Node(item)
        p.next=self.head
        self.head=p
        self.sizes+=1
        

    def search(self, item):
        p = self.head
        while  p!= None:
            if p.value == item:
                return str('Found')
            p=p.next
        return str('Not Found')

    def index(self, item):
        p =self.head
        i=0
        while p!=None:
            if p.value == item:
                return i
            p=p.next
            i+=1
        return  str("-1")

    def size(self):
        return str(self.sizes)

    def pop(self, pos):
        if pos < 0 or pos >= int(self.size()):
            return "Out of Range"
        if pos == 0 and int(self.size()) > 0:
            self.head = self.head.next
            self.sizes -= 1
            return "Success"
        else:
            p = self.head
            for i in range(0,pos-1):
                p = p.next 
            p.next =p.next.next
            self.sizes -= 1
            return "Success"
            
        

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
print("Linked List :", L)