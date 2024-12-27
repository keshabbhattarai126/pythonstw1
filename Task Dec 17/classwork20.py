winter = {1,2,12}
spring = {3,4,5}
summer = { 9,10,11}

try:
    month = int(input("Enter a month number (1–12): "))
    
    
    if month in winter:
        print(f"The season for month {month} is Winter.")
    elif month in spring:
        print(f"The season for month {month} is Spring.")
    elif month in summer:
        print(f"The season for month {month} is Summer.")
    elif month in autumn:
        print(f"The season for month {month} is Autumn.")
    else:
        print("Invalid month. Please enter a number between 1 and 12.")

except ValueError:
    print("Invalid .Enter an integer between 1 and 12.")