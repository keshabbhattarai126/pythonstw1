subject_score = float(input("Enter subject score"))
if (subject_score > 90):
    print("Congratulations !!!")
elif(50 <= subject_score <= 90):
    print("Satisfactory. You need to work on improving")
else:
    print("Please retake the test.")