class Queue:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enQueue(self,item):
        self.items.append(item)

    def deQueue(self):
        return self.items.pop(0) if self.size() != 0 else 'Empty'
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

normal, mirror = input('Enter Input (Normal, Mirror) : ').split(' ')

normal = list(normal)
mirror = list(mirror)

abomb, nItem, item = [], 0 , Queue()
for i in range(-1, -len(mirror)-1 , -1):
    abomb.append(str(mirror[i]))
    if len(abomb) > 2:
        if abomb[-1] == abomb[-2] == abomb[-3]:
            item.enQueue(str(mirror[i]))
            nItem += 1
            for j in range(3):
                abomb.pop()

bomb, boom, fail = [], 0, 0
for i, info in enumerate(normal):
    bomb.append(info)
    if len(bomb) > 2:
        if bomb[-1] == bomb[-2] == bomb[-3]:
            itempop = item.deQueue()
            if info == itempop:
                for j in range(2):
                    bomb.pop()
                fail += 1
            elif itempop == "Empty":
                for k in range(3):
                    bomb.pop()
                boom += 1
            else: 
                bomb.insert(-1, itempop)

print("NORMAL :\n", len(bomb),sep='')
print(''.join(str(i) for i in reversed(bomb)) if len(bomb) != 0 else "Empty")
print(boom, "Explosive(s) ! ! ! (NORMAL)")
if fail > 0 :
    print(f"Failed Interrupted {fail} Bomb(s)")
print("------------MIRROR------------\n\
: RORRIM\n",len(abomb),sep='')
print(''.join(str(i) for i in reversed(abomb))if len(abomb) != 0 else "ytpmE")
print(f"(RORRIM) ! ! ! (s)evisolpxE {nItem}")