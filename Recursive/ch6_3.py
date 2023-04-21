def permu(now,n):
    if(n==0):
        print(now)
        return
    temp1=now+'0'
    permu(temp1,n-1)
    temp2=now+'1'
    permu(temp2,n-1)
n = int(input('Enter Number : '))
if(n<0):
    print("Only Positive & Zero Number ! ! !")
elif(n==0):
    print('0')
else:
    permu("",n)