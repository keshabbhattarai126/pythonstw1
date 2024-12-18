age1 = int(input("Enter age of first person "))
age2 = int(input("Enter age of second person "))
age3 = int(input("Enter age of third person "))
age4 = int(input("Enter age of fourth person "))

if ( age1 > age2 and age1 > age3 and age1 > age4):
    print(f"{age1} is the oldest")
elif ( age2 > age1 and age2 > age3 and age2 > age4):
    print(f"{age2} is the oldest")
elif ( age3 > age1 and age3 > age2 and age3 > age4):
    print(f"{age3} is the oldest")
else:
    print(f"{age4} is the oldest")


