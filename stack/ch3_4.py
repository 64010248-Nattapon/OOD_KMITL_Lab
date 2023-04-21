class Stack:

    def __init__(self,list=None):
        if list==None:
            self.items=[]
        else:
            self.items=list
        
        self.sizes=0
    
    def push(self,data):
        self.items.append(data)
        self.sizes+=1
    def pop(self):
        self.sizes-=1
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def isEmpty(self):
        return self.items==[]
    def size(self):
        return self.sizes

S = Stack()
inp = input('Enter Input : ').split(',')

for i in inp:
    temp=i.split(" ")
    if temp[0]=="A":
        if S.isEmpty():
            S.push(temp[1])
            # print(S.peek())
        elif int(temp[1])>int(S.peek()):
            
            while not S.isEmpty():
                if int(temp[1])>int(S.peek()):
                    S.pop()
                else:
                    break
                
            S.push(temp[1])
            
        elif int(temp[1])<int(S.peek()):
            S.push(temp[1])
            
    elif temp[0]=="B":
        if S.isEmpty():
            print("0")
        else:
            print(S.size())
        
        
    