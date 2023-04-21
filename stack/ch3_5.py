class Stack:
    def __init__(self):
        self.lst = []
    def push(self, value):
        self.lst.append(value)
    def pop(self):
        return self.lst.pop()
    def size(self):
        return len(self.lst)
    def isEmpty(self):
        if len(self.lst) !=0:
            return False
        else :
            return True
    def delete(self,delNum):
        temp=[]
        for i in self.lst:
            if delNum != i:
                temp.append(i)
        self.lst=temp
print("******** Parking Lot ********")
m,s,o,n = input("Enter max of car,car in soi,operation : ").split(" ")
m,n = int(m),int(n)
park = Stack()
strSplit = s.split(",")
if s!='0' :
    for i in strSplit:
        park.push(int(i))
if o == "arrive":
    if len(park.lst)<m and n not in park.lst:
        park.push(n)
        print(f"car {n} arrive! : Add Car {n}")
    elif len(park.lst)>=m:
        print(f"car {n} cannot arrive : Soi Full")
    elif n in park.lst:
        print(f"car {n} already in soi")
elif o == "depart":
    if len(park.lst)>0 and n in park.lst:
        park.delete(n)
        print(f"car {n} depart ! : Car {n} was remove")
    elif len(park.lst)==0:
        print(f"car {n} cannot depart : Soi Empty")
    elif n not in park.lst:
        print(f"car {n} cannot depart : Dont Have Car {n}")
print(park.lst)