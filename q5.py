def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sumOfSeries(x,terms):
    #1-x^2/2!+x^4/4!-x^6/6!+x^8/8!-x^n/n!
    sum = 0
    for i in range(terms):
        sum += ((-1)**i)*(x**(2*i))/factorial(2*i)
    return sum

def main():
    print("Enter the value of x: ")
    x = int(input())
    print("Enter the number of terms: ")
    n = int(input())
    print("Sum of series: ", sumOfSeries(x,n))

if __name__ == "__main__":
    main()