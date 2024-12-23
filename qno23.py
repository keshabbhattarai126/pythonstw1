age = int(input("Enter age: "))
gender = input("Enter gender (m/f): ")
score = int(input("Enter academic score (out of 100): "))

if 18 <= age <= 25:
    if gender == 'm':
        if score >= 85:
            print("Full Scholarship")
        elif score >= 70:
            print("Partial Scholarship")
        else:
            print("No Scholarship")
    elif gender == 'f':
        if score >= 80:
            print("Full Scholarship")
        elif score >= 65:
            print("Partial Scholarship")
        else:
            print("No Scholarship")
