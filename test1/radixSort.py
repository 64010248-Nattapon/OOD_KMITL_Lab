from collections import deque
class Queue:
    def __init__(self):
        self.items=deque()
    
    def enQueue(self,data):
        self.items.append(data)
    
    def deQueue(self):
        return self.items.popleft()
    def isEmpty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
    
def radix_sort(data):
    max_bit=get_max(max(data))
    
    
    


def get_max(n):
    i=0
    while n>0:
        n//=10
        print(n)
        i+=1
    return i
