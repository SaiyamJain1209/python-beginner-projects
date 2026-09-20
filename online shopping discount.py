amount = float(input("Enter the total amount: "))

if amount>= 5000:
    discount = amount*0.20
    print(f"You received a discount of {discount: .2f} on the purchase of {amount: .2f}")
else:
    discount = amount*0
    
total = amount - discount

print(f"Your total amount is {total: .2f}")