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



def parenThesis(list):
    s1=Stack()
    count=0
    for ele in list:
        if ele in "([":
            s1.push(ele)
        elif ele in ")]":
            if not s1.isEmpty():    
                save=s1.pop()
                if"([".index(save) == ")]".index(ele):
                    continue
                else:
                    s1.push(save)
                    count+=1
            elif s1.isEmpty():
                # for sp in list:
                #     if sp in ")]":
                s1.push(ele) 
            
    if s1.isEmpty():
        print("0")
        print("Perfect ! ! !")
    else:
        print(len(s1.items)+count)



inp=input("Enter Input : ")
parenThesis(inp)

