sub1 = float(input("Enter marks of subject 1 "))
sub2 = float(input("Enter marks of subject 2 "))
sub3 = float(input("Enter marks of subject 3 "))
sub4 = float(input("Enter marks of subject 4 "))

total_marks = sub1 + sub2 + sub3+ sub4

percentage = (total_marks/4) * 100

if(percentage >= 70):
    grade = 'Distinction'
elif(percentage >= 60):
    grade = 'first'
elif(percentage >= 40):
    grade = 'pass'
elif(percentage < 40):
    grade = 'fail'
else:
    print("Data out of range")