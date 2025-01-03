numbers = []
user_input = int(input("How many numbers would you add: "))
i = 0
while i < user_input:
    new_var = input(f"Enter {i + 1} Number: ")
    numbers.append(new_var)
    i += 1

even = odd = 0
j = 0
while j < len(numbers):
    if int(numbers[j]) % 2 == 0:
        even += 1
    else:
        odd += 1
    j += 1

print("Total even no are:", even, ",and odd no. are:", odd)

