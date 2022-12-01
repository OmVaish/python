import matplotlib.pyplot as plt
def main():
    lst = []
    a = int(input("Enter total number of elements you need in a list : "))
    for i in range(0,a):
        b = int(input("Enter a number : "))
        lst.append(b)
    print("List is : ",lst)
    plt.hist(lst, edgecolor = "black")
    plt.xlabel("Integer")
    plt.ylabel("Count")
    plt.show()
    
main()
