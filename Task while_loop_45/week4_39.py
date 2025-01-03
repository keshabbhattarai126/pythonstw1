sum_of_odd = 0
sum_of_even = 0
i = 1
while i <= 100:
    if i % 2 != 0:
        sum_of_odd += i
    else:
        sum_of_even += i
    i += 1
print("The sum of odd numbers is: ", sum_of_odd)
print("The sum of even numbers is: ", sum_of_even)

