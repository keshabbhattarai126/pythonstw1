salary = float(input("Enter your salary: "))
year = int(input("Enter your year of service: "))
if (year > 5):
    print("Your net bonus is",salary * 0.05)
else:
    print('Not eligbile for bonus')
