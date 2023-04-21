def Fundraw(draw,num):
    if num>0:
        print("_"*(num-1)+"#"*(draw))
        Fundraw(draw+1,num-1)
    elif num<0:
        print("_"*(draw)+"#"*(-num))
        Fundraw(draw+1,num+1)

inp=int(input("Enter Input : "))
if inp>0:
    Fundraw(1,inp)
elif inp<0:
    Fundraw(0,inp)
else:
    print("Not Draw!")