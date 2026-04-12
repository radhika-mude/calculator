num1 = float(input('enter first number'))  
operator = input("select an operator +, -, *, /: ")
num2 = float(input('enter second number'))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2 
elif operator == "*":
    result = num1 * num2 
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        result = num1 / num2
print("result is", result)