try:
    percentage = float(input("Enter percentage: "))
    if percentage < 40:
        print("Failed")
    elif 40 <= percentage < 55:
        print("Fair")
    elif 55 <= percentage < 65:
        print("Good")
    elif percentage >= 65:
        print("Excellent")
    else:
        print("Invalid percentage.")
except ValueError:
    print("Invalid input! Please enter number.")
