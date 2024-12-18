days = int(input("Enter number of days: "))
if( days < 5):
    charge = 'Rs 2/day'
elif(6 <= days <= 10):
    charge = 'Rs 3/day'
elif(11 <= days <= 15 ):
    charge = 'Rs 4/day'
elif(days > 15):
    charge = 'Rs 5/day'
else:
    charge ='invalid input, out of range'
print(f" Your library charge rate is {charge}")