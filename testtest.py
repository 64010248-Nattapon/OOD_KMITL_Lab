def reCersive(n):
    if n==0:
        return n
    else:
        return n*reCersive(n-1)
    
print("f : ",str(reCersive(3)))