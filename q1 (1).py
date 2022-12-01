def triangle():
    side1 = float(input("Enter the side: "))
    side2 = float(input("Enter the side: "))
    side3 = float(input("Enter the side: "))
    assert side1+side2>side3 and side1+side3>side2 and side2+side3>side1, "Invalid triangle"
    s=(side1+side2+side3)/2
    area=(s*(s-side1)*(s-side2)*(s-side3))**0.5
    perimeter=side1+side2+side3
    return (area,perimeter)
t=triangle()
print("Area of triangle is: ",t[0])
print("Perimeter of triangle is: ",t[1])

