num = int(input("Enter any integer number: "))
if (num % 2 == 0):
    print(f"{num} is divisible by 2.")
    if (num % 5 == 0):
        print(f'{num} is divisible by 5')
    else:
        print (f'{num} is not divisible by 5')
else:
    print(f'{num} is not divisible by 2')