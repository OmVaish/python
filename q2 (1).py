def commisionCalculate(sales):
    totalSales=sales[1]+sales[2]+sales[3]+sales[0]
    commision=totalSales*0.05
    if totalSales>=80000:
        remark="Excellent"
    elif 60000<=totalSales<80000:
        remark="Good"
    elif 40000<=totalSales<60000:
        remark="Average"
    else:
        remark="Work Hard"
    return [totalSales,commision,remark]
sales=[]
for i in range(1,5):
    sales.append(int(input("Enter the sales of week:")))
result=commisionCalculate(sales)
print("Total sales of 4 weeks is: ",result[0])
print("Commision of 4 weeks is: ",result[1])
print("Remark of 4 weeks is: ",result[2])
