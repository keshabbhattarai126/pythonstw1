age = int(input("Enter age"))
gender = input("Enter gender (m/f)")
income = float(input("Enter income"))

if (18 <= age <60 ):
    if( gender=='m'):
        if(income > 1000000):
            tax = 0.3 * income
        elif(500000 < income <= 1000000):
            tax = 0.2 * income
        elif(income <= 500000):
            tax = 0.1 * income
    if( gender=='f'):
        if(income > 1000000):
            tax = 0.25 * income
        elif(500000 < income <= 1000000):
            tax = 0.15 * income
        elif(income <= 500000):
            tax = 0.05 * income
elif (age >=60):
    if (gender == 'm' or gender == 'f'):
        if(income > 1000000):
            tax = 0.2 * income
        elif(income <= 1000000):
            tax = 0.1 * income 

print(f"Tax: {tax}")