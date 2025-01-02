
i = 1
while (i != 0 ):
    age = int(input("Enter age: "))
    if( age < 18 ):
        print("You are a minor")
    elif(10 <= age <= 60):
        print("You are an adult")
    elif( age > 60):
        print("You are a senior citizen")
    choice = input("Press stop to exit")
    if(choice == 'stop'):
        break
    else:
        i = i + 1


