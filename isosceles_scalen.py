side1=int(input("enter the number"))
side2=int(input("enter the number"))
side3=int(input("enter the number"))
if side1==side2==side3:
    print("it is equilateral trangle")
elif side1==side2 or side1==side3:
    print("it is isosceles trangle")
else:
    print("it is scalene trangle")
