number = 10

while True:
    guess = int(input("Enter a number: "))
    
    if guess == number:
        print("it's a correct guess")
        break
    elif guess > number:
        print("it's too high")
    else:
        print("it's too low")
        