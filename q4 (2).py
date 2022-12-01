def setOfDigits(n):
    digits = []
    while(n>0):
        digit = n%10
        if digit not in digits:
            digits.append(digit)
        n = n//10
    return digits
n=int(input("Enter the number: "))
print(setOfDigits(n))