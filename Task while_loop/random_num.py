import random

i = 1
while (i != 0):
    a = random.randint(1,30)
    b = random.randint(1,30)
    multiplication_user = int(input("Enter the result"))
    multiplication = a * b

    if(multiplication == multiplication_user):
        print("Correct Answer")
    else:
        print("Wrong answer")
    choice = input("Do you want to Continue (y/n)")
    if(choice == 'y'):
        i = i+1
    elif choice == 'n':
        i = 0