num = int(input("Enter number to calculate factorial: "))
fact = 1
for i in range(num, 1, -1):
    fact = fact * i
print(f"The factorial of {num} is {fact}")
