time = float(input("Enter experience time period (in years) in this office "))
if (time > 10):
    bonus = '10 %'
elif ( 6 <= time <= 10):
    bonus = '8 %'
elif ( time > 6):
    bonus = '5 %'
else:
    bonus = 'out of range'
print( f"Your bonus is {bonus} .")
