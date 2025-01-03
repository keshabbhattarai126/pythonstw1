number = int(input("Enter a number: "))
count = 0
i = 1
while i <= number:
    if number % i == 0:
        count += 1
    if count > 2:
        break
    i += 1
if count == 2:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")

