num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+ - * / % ** //): ")
if(op== '+'):
    print(f"Your answer is: {num1 + num2}")
elif(op== '-'):
    print(num1 - num2)
elif(op== '*'):
    print(f"Your answer is: {num1 * num2}")
elif(op== '/'):
    print(f"Your answer is: {num1 / num2}")
elif(op== '%'):
    print(f"Your answer is {num1 % num2}")
elif(op== '**'):
    print(f"Your answer is {num1 ** num2}")
elif(op== '//'):
    print(f"Your answer is {num1 // num2}")
else:
    print("Please enter valid operator")