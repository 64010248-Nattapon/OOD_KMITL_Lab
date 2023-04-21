def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
inp=int(input("Enter Number : "))
print(f'fibo({inp}) = {fibo(inp)}')