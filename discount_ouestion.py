quantity1=int(input("enter the age"))
quantity2=int(input("enter the age"))
discount1=quantity/100*5
discount2=quantity/100*15
if quantity1>=800 and quantity2>=1000:
    total_cost=quantity1-discount
    print("total cost")
else:
    print("no total cost")
