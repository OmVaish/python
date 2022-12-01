def length():
    str = input("Enter a string : ")
    print ("Length of the string : ",len(str))

def maximum():
    str1 = input("Enter the first string : ")
    str2 = input("Enter the second string : ")
    str3 = input("Enter the third string : ")
    print ("Maximum of three strings : ",max(str1,str2,str3))

def replace():
    str = input("Enter a string : ")
    x = "aeiouAEIOU"
    for i in str:
        if i in x:
            str = str.replace(i,"#")
    print("String after replacement : ",str)

def count():
    c = 0
    str = input("Enter a string : ")
    for i in str:
        if(i.isalpha()):
            c += 1
    print("Number of alphabets : ",c)

def palindrom():
    str = input("Enter a string : ")
    value = str == str[::-1]

    if(value):
        print("The given string is a palindrom.")
    else:
        print("The given string is not a palindrom.")

def main():
    while(1):
        print("Enter 1 for calculating length : ")
        print("Enter 2 for calculating maximum : ")
        print("Enter 3 for replace : ")
        print("Enter 4 for count : ")
        print("Enter 5 for checking palindrom : ")
        y = int(input("Enter choice 1 to 5 : "))
        if(y == 1):
            length()
            print()
        elif(y == 2):
            maximum()
            print()
        elif(y == 3):
            replace()
            print()
        elif(y == 4):
            count()
            print()
        elif(y == 5):
            palindrom()
            print()
        else:
            if(y == 6):
                print()
                print("Program terminate.")
                break;

main()
