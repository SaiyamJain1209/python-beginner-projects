num1 = float(input("Enter first number: "))
num2 = float(input("ENter second number: "))

operator = input("Enter operator(+,-,*,/,//,%,**): ")
def smart_calculator(num1, num2, operator):
    match operator:
        case '+':
            return num1 + num2 
        case '-':
            return num1- num2
        case '*':
            return num1 *num2
        case '/':
            return num1/ num2
        case '//':
            return num1 // num2
        case '%':
            return num1 % num2 
        case '**':
            return num1 **num2 
        case _:
            return 'Invalid operator'
    
result = smart_calculator(num1,num2, operator)
print(f"The result of {num1} {operator} {num2} is: {result}")