class Queue:
    def __init__(self,list=None):
        if list==None:
            self.items=[]
        else:
            self.items=list
            
    def aslist(self):
        return self.items
    
    def __str__(self):
        return str(self.items)
    
    def enqueue(self,data):
        self.items.append(data)
    
    def dequeue(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items==[]
    
    def peek(self):
        if not self.isEmpty():
            return self.items[0]
    def size(self):
        return len(self.items)

time = 1
people = str(input("Enter people : "))

c1timerun = False
c2timerun = False
timeC1 = 0
timeC2 = 0
q = Queue()
cashier1=Queue()
cashier2=Queue()
for i in people:
    q.enqueue(i)

while q.isEmpty() != True  :
    if timeC1%3==0 and timeC1!= 0:
        cashier1.dequeue()
    if timeC2%2==0 and timeC2!= 0:
        cashier2.dequeue()
    if cashier1.size()==5:
        cashier2.enqueue(q.peek())
    else:
        cashier1.enqueue(q.peek())
   
    if cashier1.isEmpty() != True:
        c1timerun = True
    else :
        c1timerun = False
    if cashier2.isEmpty() != True:
        c2timerun = True
    else :
        c2timerun = False
    q.dequeue()
    print( time, q.aslist(), cashier1.aslist(),cashier2.aslist())
    if c1timerun:
        timeC1+=1
    if c2timerun:
        timeC2+=1
    time+=1

