def main():
    t1 = (1,2,5,7,9,2,4,6,8,10)
    t2 = (11,13,15)
    t3 = []
    for i in range(0,len(t1)):
        if(t1[i] % 2 == 0):
            t3.append(t1[i])
    print ("First tuple is : ",t1)
    print ("Second tuple is : ",t2)
    print ("Third tuple is : ",tuple(t3))
    print ("Tuple after concatination of first and second tuple is : ",t1+t2)
    print("Maximum value in first tuple : ",max(t1))
    print("Minimum value in first tuple : ",min(t1))

main()
