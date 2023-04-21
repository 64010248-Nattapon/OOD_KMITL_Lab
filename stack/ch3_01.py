class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        return str(self.items)

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


s = Stack()
inp = input("Enter Input : ")
op = "(["
cl = ')]'
for i in inp:
    if i in op:
        s.push(i)
    elif i in cl:
        if not s.isEmpty():
            peek = s.peek()
            if op.index(peek) == cl.index(i):
                s.pop()
            else:
                s.push(i)
        elif s.isEmpty():
            s.push(i)


if s.isEmpty():
    print("0")
    print("Perfect ! ! !")
else:
    print(len(s.items))
