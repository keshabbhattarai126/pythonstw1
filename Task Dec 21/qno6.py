num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 > num2:
    if num1 > num3:
        greatest = num1
    else:
        greatest = num3
else:
    if num2 > num3:
        greatest = num2
    else:
        greatest = num3

print(f'{greatest} is the greatest number.')
