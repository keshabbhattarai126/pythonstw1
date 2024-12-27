start = int(input("Enter starting number"))
stop = int(input("Enter stopping number"))
sum = 0
for i in range(start, stop + 1):
    sum = sum + i
print(f"The sum is {sum}")  