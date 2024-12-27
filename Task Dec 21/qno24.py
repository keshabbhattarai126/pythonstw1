age = int(input("Enter age: "))
gender = input("Enter gender (m/f): ")
experience = int(input("Enter years of experience: "))

if 21 <= age <= 35:
    if gender == 'm':
        if experience >= 5:
            print("Senior Developer")
        else:
            print("Junior Developer")
    elif gender == 'f':
        if experience >= 5:
            print("Senior Analyst")
        else:
            print("Junior Analyst")
elif age > 35:
    print("Manager Role")
