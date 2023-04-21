class Stack:

    def __init__(self,list=None):
        if list==None:
            self.items=[]
        else:
            self.items=list
        self.sizes=0
    def push(self, value):
        self.items.append(value)
        self.sizes+=1
    def pop(self):
        self.sizes-=1
        return self.items.pop()
    def size(self):
        return self.sizes
    def isEmpty(self):
        return self.items==[]


inp = input('Enter Input : ').split()

S = Stack()
combo=0
for i in inp:
    if S.size()<2:
        S.push(i)
    else:
        S.push(i)
        pop3,pop2,pop1=S.pop(),S.pop(),S.pop()
        if not pop3==pop2==pop1:
            S.push(pop1)
            S.push(pop2)
            S.push(pop3)
        else:
            combo+=1

print(S.size())
if S.isEmpty():
    print("Empty")
else:
    while not S.isEmpty():
        print(S.pop(),end="")
    print()
if combo>1:
    print(f'Combo : {combo} ! ! !')