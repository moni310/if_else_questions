age1=int(input("enter the age"))
age2=int(input("enter the age"))
age3=int(input("enter the age"))
if age1>=age2 and age1>=age3:
    print("age1 is oldest or youngest")
elif age2>=age1 and age2>=age3:
    print("age2 is youngest or oldest")
elif age3>=age1 and age3>=age2:
    print("age3 is youngest or oldest")
else:
    print("age1 is youngest than age2")