number = int(input("Enter a number: "))
sum_of_even = 0
i = 0
while i <= number:
    if i % 2 == 0:
        sum_of_even += i
    i += 1
print("The sum of even numbers is: ", sum_of_even)

