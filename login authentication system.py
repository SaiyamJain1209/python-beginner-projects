name = input("Enter your name: ")
password = input("Enter your password: ")

correct_name = "admin"
correct_password = "admin@123"

attempts = 3

while attempts>=1:
    if name == correct_name and password == correct_password:
        print("Login successfully")
        break
    else:
        print("Invalid username or password")       
        attempts -= 1
        print(f"You have {attempts} attempts left".format(3 - attempts))
        name = input("Enter your name: ")
        password = input("Enter your password: ")
if attempts == 0:
    print("You have exceed the maximum attempts limit. try again in 30 seconds")

                  