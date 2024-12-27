age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ")
days = int(input("Enter number of days: "))

if 18 <= age < 30:
    if gender == 'M':
        wage_per_day = 700
    elif gender == 'F':
        wage_per_day = 750
    else:
        print("Invalid gender.")
else:
    if 30 <= age <= 40:
        if gender == 'M':
            wage_per_day = 800
        elif gender == 'F':
            wage_per_day = 850
        else:
            print("Invalid gender.")
    else:
        print("Age not eligible for wages.")
        wage_per_day = None

if wage_per_day is not None:
    total_wages = wage_per_day * days
    print(f"Total wages: {total_wages}")
