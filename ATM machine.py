card = input("Please insert your card: ")
language = "English"
    
pin = int(input("Enter your 4 digit pin: "))

if 0000 <= pin <= 9999:
    print("Pin accepted")

    
    menu = input("Please select your transection: 1. Balance \n 2. Withdraw \n 3. Deposit \n 4. Exit \n: ")
    balance = 100000

    if menu == "1":
        print("Your balance is: ", balance)
    
    elif menu == "2":
        withdraw = int(input("Enter amount to withdraw: "))
        if withdraw <= balance:
            balance -= withdraw
            print("Please collect your cash. Your new balance is: ", balance)
        else:
            print("Insufficient balance. Your balance is: ", balance)
        
    elif menu == "3":
        deposit = int(input("Enter amount to deposit: "))
        balance += deposit
        print("Your total balance is: ", balance)
    
    else:
        print("Thank you for using our ATM. Have a nice day!")
    
    total = balance
    
    
    take = input("Remove your card: ")
    
else:
    print("Invalid pin. Please try again.")

print("Please enter your card: ", card)
print("Your language is: ", language)
print("Please enter your pin: ", pin)
print("Your selected transection is: ", menu)
print("Your balance is: ", total)
print("Please remove your card: ", take)