age = int(input("Enter age: "))
gender = input("Enter gender (m/f): ")
membership = input("Enter membership type (Monthly/Yearly): ")

if 18 <= age < 30:
    if gender == 'm':
        if membership == "Monthly":
            price = 50
        elif membership == "Yearly":
            price = 500
    elif gender == 'f':
        if membership == "Monthly":
            price = 45
        elif membership == "Yearly":
            price = 450
elif 30 <= age <= 50:
    if membership == "Monthly":
        price = 60
    elif membership == "Yearly":
        price = 600
elif age > 50:
    if membership == "Monthly":
        price = 40
    elif membership == "Yearly":
        price = 400

print(f"Membership Price: Rs{price}")
