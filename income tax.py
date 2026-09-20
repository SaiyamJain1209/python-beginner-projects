salary = int(input("Enter your Salary: "))

if salary <= 400000:
    tax = 0
elif salary <=800000:
    tax = salary*0.05
elif salary <= 1200000:
    tax = 20000 + (salary - 800000)*0.1
elif salary <= 1600000:
    tax = 60000 + (salary - 1200000)*0.15
elif salary <= 2000000:
    tax = 120000 + (salary - 1600000)*0.2
elif salary <= 2400000:
    tax = 200000 + (salary - 2000000)*0.25
else:
    tax = 300000 + (salary - 2400000)*0.3
    
print("Your Income Tax is: ", tax) 
