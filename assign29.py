age = int(input("Enter your age: "))
has_degree = input("Do you have a degree? (Y/N): ")

if age >= 18:
    if has_degree == 'Y':
        work_experience = int(input("Enter your years of work experience: "))

        if work_experience > 3:
            print("Highly Eligible.")
        elif 1 <= work_experience <= 3:
            print("Eligible.")
        else:
            print("Under Review.")
    else:
        print("You must have a degree.")
else:
    print("You must be at least 18 years old to be eligible.")
