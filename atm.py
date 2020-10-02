print("welcome to SBI")
print("enter your atm card")
print("what you want,")
lan=(input("enter the lan"))
pin=int(input("enter the pin"))
ammount=int(input("enter the ammount"))
if lan=="english":
    if pin== 5765 or pin==2345 or pin==4876:
        if ammount<10000:
            print("avilable")
        else:
            print("sorry")
else:
    print("invalid")            