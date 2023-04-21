class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
        self.sizes=0
    
    def __str__(self):
        return str(self.items)
    
    def push(self,data):
        self.items.append(data) 
        self.sizes += 1 
    def pop(self):
        if not self.isEmpty():
            self.sizes -=1
            return self.items.pop()
        else:
            print("Stack is Empty")

    def peek(self):   
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items ==[]


    def size(self):
        return self.sizes
    
def postFixCal(ele):
    s=Stack()
    for i in ele:
        if i in '0123456789':
            s.push(int(i))
        else:
            a=s.pop()
            b=s.pop()
            if i == '+':
                s.push(b+a)
            elif i == '-':
                s.push(b-a)
            elif i == '*':
                s.push(b*a)
            elif i == '/':
                s.push(b/a)
    
    return s.pop()

inp=input("enter postfix:")
print(postFixCal(inp))
                