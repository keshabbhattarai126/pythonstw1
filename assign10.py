marks = float(input("Enter marks "))
if(marks < 25):
    grade = 'D'
elif (25 <= marks < 45 ):
    grade = 'C'
elif (45 <= marks < 50 ):
    grade = 'B'
elif (50 <= marks < 60 ):
    grade = 'B+'
elif (60 <= marks < 80 ):
    grade = 'A'
elif (marks >= 80 ):
    grade = 'A+'
else:
    grade ='out of range'
print(f"Your grade is {grade}")
