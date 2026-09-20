height = float(input('Enter your height in feet: '))
weight = float(input('Enter your weight in kg: '))

feet = height * 0.3048

bmi = weight/feet**2

if bmi <= 18.5:
    print(f'your BMI is {bmi} and you are under weight')
elif 18.5< bmi < 25:
    print(f'your BMI is {bmi} and your weight is normal')
elif 25 <= bmi <30:
    print(f'your BMI is {bmi} and you are overweight')
else:
    print(f'your BMI is {bmi} and your weight is obese')
    
