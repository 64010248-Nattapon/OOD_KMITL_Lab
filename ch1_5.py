print("*** Fun with countdown ***")
list = [int(item) for item in input("Enter List : ").split()]
listSort=[]
finalList=[]
i=0
count=0
temp= list[0]
while i!=len(list):
    if temp==list[i]:
        listSort.append(temp)
        temp-=1
    else :
        temp = list[i]
        listSort=[]
        listSort.append(temp)
        temp-=1
    if temp == 0 :
        finalList.append(listSort)
        listSort=[]
        count+=1
    i+=1
    

resultLst=[]
resultLst.append(count)
resultLst.append(finalList)
print(resultLst)