nested-age=int(input("enter the age"))
sex=input("enter sex")
maritial=input("enter martial")
if sex==male:
    if age<=40:
        print("work any where")
    elif sex==male:
        if age<=60:
            print("work only in urban")
elif sex==female:
    print("work anywhere")
else:
    print("error")