num1 = float(input("Enter first number "))
num2 = float(input("Enter second number"))

if( num1 > num2):
    print(f"{num1} is greater")
elif (num1 == num2):
    if(num1 > 0):
        print(f"{num1} is positive")
    elif(num1 == 0):
        print(f"{num1} is zero")
    else:
        print(f"{num1} is negative")
else:
    print(f"{num2} is greater")
