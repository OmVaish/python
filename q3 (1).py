def fibo(n):
    if(n==1):
        return 0
    if(n==2):
        return 1
    return fibo(n-1)+fibo(n-2)

def nthFiboandFact(n):
    fib=fibo(n)
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return[fib,fact]   

n = int(input("Enter the number: "))

print(nthFiboandFact(n))
    