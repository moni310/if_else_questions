num1=int(input("enter the number"))
operation=input("enter the sine")
num2=int(input("enter the number"))
if operation=="+":
   sum=num1+num2
   print("sum",sum)
elif operation=="-":
   sub=num1-num2
   print("sub",sub)
elif operation=="%":
    mod=num1%num2
    print("mod",mod)
else:
    print("no operator")