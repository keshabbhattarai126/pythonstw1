number = input("Enter a number: ")
armnum = 0
i = 0
while i < len(number):
    armnum += int(number[i]) ** len(number)
    i += 1
if int(number) == armnum:
    print(number, " is Armstrong Number.")
else:
    print(number, "is not a Armstrong number.")

