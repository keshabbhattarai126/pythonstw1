age = int(input("Enter age: "))
gender = input("Enter gender (m/f): ")
show_type = input("Enter show type (Matinee/Evening): ")

if age < 12:
    if show_type == "Matinee":
        ticket = 500
    elif show_type == "Evening":
        ticket = 700
elif 12 <= age < 60:
    if gender == 'm':
        if show_type == "Matinee":
            ticket = 800
        elif show_type == "Evening":
            ticket = 1000
    elif gender == 'f':
        if show_type == "Matinee":
            ticket = 700
        elif show_type == "Evening":
            ticket = 900
elif age >= 60:
    ticket = 600

print(f"Ticket Price: Rs{ticket}")
