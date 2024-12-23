num = int(input("Enter a number"))
if ( num % 2 == 0 and num % 7 == 0):
    print("Double Seven")
elif ( num % 2 == 0 and num % 7 != 0):
    print("ैEven")
elif (num % 7 == 0 and num % 2 != 0):
    print("Lucky Seven")
else:
    print(num)