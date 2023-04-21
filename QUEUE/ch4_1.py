class Queue:
    def __init__(self,list=None):
        if list==None:
            self.items=[]
        else:
            self.items=list
    
    def __str__(self):
        return str(self.items)
    
    def enQueue(self,data):
        self.items.append(data)
    
    def deQueue(self):
        return self.items.pop(0)
       
    def isEmpty(self):
        return self.items==[]
    
    def size(self):
        return len(self.items)
q=Queue()
inp=input("Enter Input : ").split(',')
for i in inp:
    temp=i.split(" ")
    if temp[0] =="E":
        q.enQueue(temp[1])
        save1=q.items.index(temp[1])
        print(f'Add {temp[1]} index is {save1}')    
    elif temp[0]=="D":
        if not q.isEmpty():
            savede=q.deQueue()
            print(f'Pop {str(savede)} size in queue is {len(q.items)}')
        else:
            print("-1")
        
if not q.isEmpty():        
    print(f'Number in Queue is :  {q.items}')
else:
    print("Empty")


        
        
    
        