class Queue:
    def __init__(self):
        self.lst=[]
    def enQueue(self,num):
        for val in self.lst[-1::-1]:
            if num[0] == val[0]:
                if self.lst.index(val) == self.size() - 1:
                    break
                self.lst.insert(self.lst.index(val) + 1, num)
                return
        self.lst.append(num)
    def deQueue(self):
        return self.lst.pop(0)
    def size(self):
        return len(self.lst)
    def isEmpty(self):
        return self.lst==[]
    
inp,op = input('Enter Input : ').split('/')
lst = dict()
for i in inp.split(','):
    i = i.split()
    lst[i[1]] = i[0]
queue = Queue()
for d in op.split(','):
    d = d.split()
    if d[0] == 'D':
        if queue.isEmpty():
            print("Empty")
        else:
            print(int(queue.deQueue()[1]))
    elif d[0] == 'E':
        d[0] = lst[d[1]]
        queue.enQueue(d)