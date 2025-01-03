number = int(input("Enter a number: "))
sum_of_odd = 0
i = 0
while i <= number:
    if i % 2 != 0:
        sum_of_odd += i
    i += 1
print("The sum of odd numbers is: ", sum_of_odd)

