class node:
    def __init__(self,data,next = None ):
        self.data=data
        self.next=next
        self.prev=None

def createList(l=[]):
    head=None
    tail=None
    
    if len(l)==1:
        n=node(int(l[0]))
        head=n
        tail=n
    else:
        n=node(int(l.pop(0)))
        head=n
        tail=n
        for i in l:
            t=node(int(i))
            tail.next=t
            t.prev=tail
            tail=t
    
    return head
            

def printList(H):
    while H != None:
        print(H.data,end=' ')
        H=H.next
    print()
    ### Code Here ###

def mergeOrderesList(p,q):
    lst1=p
    lst2=q
    head=None
    if lst1.data < lst2.data:
        head=node(lst1.data)
        lst1=lst1.next
    else:
        head=node(lst2.data)
        lst2=lst2.next
    tail=head
    while lst1!=None and lst2!=None:
        if lst1.data < lst2.data:
            n=node(lst1.data)
            tail.next = n
            n.pre=tail
            tail = n
            lst1=lst1.next
        else:
            n=node(lst2.data)
            tail.next = n
            n.pre=tail
            tail = n
            lst2=lst2.next
    while lst1 !=None:
        n=node(lst1.data)
        tail.next = n
        n.pre=tail
        tail = n
        lst1=lst1.next
    while lst2!=None:
        n=node(lst2.data)
        tail.next = n
        n.pre=tail
        tail = n
        lst2=lst2.next
    return head
    ### Code Here ###

#################### FIX comand ####################   
# input only a number save in L1,L2
inp=input("Enter 2 Lists : ").split(" ")
L1=[item for item in inp[0].split(',')]
L2=[item for item in inp[1].split(",")]
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)