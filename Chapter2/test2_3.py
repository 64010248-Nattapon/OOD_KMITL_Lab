def newRange(*n): 
    k=[]
    if len(n)==1:
        s=0.0
        while s<n[0]:
            k.append(s)
            s+=1
    elif len(n)==2:
        s=n[0]
        while s<n[1]:
            k.append(s)
            s+=1
    else:
        s=n[0]
        while s<n[1]:
            k.append(s)
            s+=n[2]
    return k
print("*** New Range ***")
inp=[float(i) for i in input("Enter Input : ").split()]
if len(inp)==1:
    l=newRange(inp[0])
elif len(inp)==2:
    l=newRange(inp[0],inp[1])
else:
    l=newRange(inp[0],inp[1],inp[2])
for i in range(len(l)):
    l[i]=float("{:.3f}".format(l[i]))
print(tuple(l))