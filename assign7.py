cost = float(input("Enter cost price of bike"))
if( cost > 100000):
    tax = cost * 0.15
elif(50000 > cost >= 100000):
    tax = cost * 0.1
elif(cost<= 50000):
    tax = cost * 0.5
else:
    "out of range."
    