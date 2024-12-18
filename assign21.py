total = int(input("Enter total number of days "))
absent = int(input("Enter toal number of days absent "))
percentage = ((total-absent)/total)*100
if(percentage < 75):
    print("You are ineligible to sit in exam")
else:
    print("You are eligible to sit in exam")
    