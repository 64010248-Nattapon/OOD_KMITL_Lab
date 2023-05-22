def sort(lis):
    for i in range(len(lis)):
        for j in range(len(lis)):
            if j+1 < len(lis) and lis[j]>lis[j+1]:
                temp=lis[j]
                lis[j]=lis[j+1]
                lis[j+1]=temp
inp=[int(e) for e in input('Enter Input : ').split()]
BBSort = inp.copy()
sort(BBSort)
if inp == BBSort:
    print('Yes')
else :
    print('No')