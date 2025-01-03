number = int(input("Enter a number: "))
perfect_num = 0
i = 1
while i < number:
    if number % i == 0:
        perfect_num += i
    i += 1

if perfect_num == number:
    print(number, " is a Perfect number.")
else:
    print(number, " is not a Perfect number.")

