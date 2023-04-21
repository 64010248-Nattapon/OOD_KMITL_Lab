def ReverseSort(l,i=0):
    s
    if len(l)==0:
        return 1
    elif len(s)==0 or i==len(s): 
        s.append(l[0])
        return ReverseSort(l[1:])
    elif l[0]<s[i]:
        return ReverseSort(l,i+1)
    else:
        s.insert(i,l[0])
        return ReverseSort(l[1:])

l = [int(i) for i in input("Enter your List : ").split(",")]
s=[]
ReverseSort(l)
print("List after Sorted :",s)