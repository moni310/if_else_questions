quantity=int(input("Enter your quantity: "))
discount=quantity/100*10
if quantity>=1000:
    total_cost=quantity-discount
    print("Total cost",total_cost)
else:
    print("no discount")