number = int(input("Enter a number: "))
fact = 1
i = 1
while i <= number:
    fact *= i
    i += 1
print("The factorial for ", number, " is ", fact)

