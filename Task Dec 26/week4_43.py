number = int(input("Enter a number: "))
perfect_num = 0

for i in range(1,number):
    if number % i == 0:
        perfect_num += i

if perfect_num == number:
    print(number," is a Perfect number.")
else:
    print(number," is not a Perfect number.")