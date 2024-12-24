num = int(input("Enter number to reverse it: "))

rev_num = 0

for i in range(len(str(num))):
    each_digit = num % 10
    rev_num = rev_num * 10 + each_digit
    num //= 10
print(f"The reverse number is {rev_num}")