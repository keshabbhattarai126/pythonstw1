user_input = int(input("Enter a number: "))
sum = 0
while (user_input != 0):
    sum = sum + user_input
    if (user_input != 0):
        user_input = int(input("Enter a number: "))
print("Sum = ",sum)
