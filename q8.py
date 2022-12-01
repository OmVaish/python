def main():
    print("Enter 1 for numeric list : ")
    print("Enter 2 for string list : ")
    x = int(input("Enter a choice : "))
    
    if(x == 1):
        lst = []
        lst2 = []  
        a = int(input("Enter total number of elements you need in a list : "))
        for i in range(0,a):
            b = int(input("Enter number for list : "))
            lst.append(b)
        print("List is : ",lst)
    
        if all(isinstance(item, int)for item in lst2):
            print("List only have numbers.")
            for i in range(0,len(lst)):
                if(lst[i] % 2 != 0):
                    lst2.append(lst[i])
            print("List with odd numbers : ",lst2)
    
        lst3 = lst
        lst3.reverse()
        print("Reversed list : ",lst3)
        lst.reverse()
        
        ele = int(input("Enter a number which you want to search : "))
        if ele in lst:
            print("Number found.")
        else:
            print("Number not found.")

        ele = int(input("Enter a number which you want to remove : "))
        if ele in lst:
            lst.remove(ele)
        print("List after deleting a number : ",lst)

        lst.sort()
        lst.reverse()
        print("List in decending order",lst)

        lst4 = []
        c = int(input("Enter total number of elements you need for second list : "))
        for i in range(0,c):
            d = int(input("Enter number for list : "))
            lst4.append(d)
        if(len(lst)>len(lst4)):
            for i in range (0,len(lst)):
                if lst[i] in lst4:
                    print("Comman number is : ",lst[i], end = " ")
        else:
            for i in range (0,len(lst4)):
                if lst4[i] in lst:
                    print("Comman number is : ",lst4[i], end = " ")
                    
    elif(x == 2):
        lst = [] 
        a = int(input("Enter total number of string values you need in a list : "))
        for i in range(0,a):
            b = input("Enter string values : ")
            lst.append(b)
        print("List is : ",lst)
        
        print("Largest string in the list : ",max(lst))
        
        ele = input("Enter a string value which you want to search : ")
        if ele in lst:
            print("String found.")
        else:
            print("String not found.")

        ele = input("Enter a string value which you want to remove : ")
        if ele in lst:
            lst.remove(ele)
        print("List after deleting a string : ",lst)

        lst.sort()
        lst.reverse()
        print("List in decending order",lst)

        lst2 = []
        c = int(input("Enter total number of string values you need for second list : "))
        for i in range(0,c):
            d = input("Enter string value for list : ")
            lst2.append(d)
        if(len(lst)>len(lst2)):
            for i in range (0,len(lst)):
                if lst[i] in lst2:
                    print("Comman string is : ",lst[i], end = " ")
        else:
            for i in range (0,len(lst2)):
                if lst2[i] in lst:
                    print("Comman string is : ",lst2[i], end = " ")

    else:
        print("Invalid choice.")
        
    
main()
