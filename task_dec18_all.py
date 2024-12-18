#Submitted by Keshab Bhattarai 37B AI


#  Q. No.1  
#Write a Python Program to swap variable

a = int(input("Enter first value"))
b = int(input("Enter second value"))
a,b = b,a
print(a,b)

#  Q. No.2  
print("Welcome to the Treasure Land")

direction = input("Enter direction (left/right)")

if direction == 'right':
    print("Game Over")
elif direction == 'left':
    decision1= input("Do you want to swim or wait? Type(swim/wait)")
    if(decision1 == 'swim'):
        print("Game Over")
    elif decision1 == 'wait':
        color = input("Choose a color? (blue/red/yellow)")
        if(color == 'blue' or color == 'red'):
            print("Game Over")
        elif(color == 'yellow'):
            print("You win")
        else:
            print("Invalid Option. Type (red/blue/yellow)")
    else:
        print("Invalid option. Type(swim/wait)")
else:
    print("Invalid option. Type (left/right)")

#  Q. No.4  
num = int(input("Enter a number"))
if (num<0):
    print("Negative")
elif (num == 0):
    print ("Zero")
else:
    print("Positive")


#  Q. No.5  
num = int(input("Enter a number"))
if (num % 2 ==0):
    print(f"{num} is an even number")
else:
    print(f"{num} is odd number")

#  Q. No.6  
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

#  Q. No.7  
cost = float(input("Enter cost price of bike"))
if( cost > 100000):
    tax = cost * 0.15
elif(50000 > cost >= 100000):
    tax = cost * 0.1
elif(cost<= 50000):
    tax = cost * 0.5
else:
    "out of range."
    

#  Q. No.8  
age1 = int(input("Enter age of first person "))
age2 = int(input("Enter age of second person "))
age3 = int(input("Enter age of third person "))
age4 = int(input("Enter age of fourth person "))

if ( age1 < age2 and age1 < age3 and age1 < age4):
    print(f"{age1} is the youngest")
elif ( age2 < age1 and age2 < age3 and age2 < age4):
    print(f"{age2} is the youngest")
elif ( age3 < age1 and age3 < age2 and age3 < age4):
    print(f"{age3} is the youngest")
else:
    print(f"{age4} is the youngest")




#  Q. No.9  
age1 = int(input("Enter age of first person "))
age2 = int(input("Enter age of second person "))
age3 = int(input("Enter age of third person "))
age4 = int(input("Enter age of fourth person "))

if ( age1 > age2 and age1 > age3 and age1 > age4):
    print(f"{age1} is the oldest")
elif ( age2 > age1 and age2 > age3 and age2 > age4):
    print(f"{age2} is the oldest")
elif ( age3 > age1 and age3 > age2 and age3 > age4):
    print(f"{age3} is the oldest")
else:
    print(f"{age4} is the oldest")


#  Q. No.10  
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


#  Q. No.11  
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


#  Q. No.12  
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

#  Q. No.13  
salary = float(input("Enter your salary: "))
year = int(input("Enter your year of service: "))
if (year > 5):
    print("Your net bonus is",salary * 0.05)
else:
    print('Not eligbile for bonus')


#  Q. No.14  
import math
radius = float(input("Enter radius of circle"))
area = math.pi * math.pow(radius,2)
print(f"The area of circle is {area}")

#  Q. No.15  
no_of_std_class_a = int(input("Enter the number of students in class A: "))
no_of_std_class_b = int(input("Enter the number of students in class B: "))
no_of_std_class_c = int(input("Enter the number of students in class C: "))


classes = {
    "Class A": no_of_std_class_a,
    "Class B": no_of_std_class_b,
    "Class C": no_of_std_class_c
}

total_desks = 0

for class_name, no_of_students in classes.items():
   
    if no_of_students % 2 == 0:
        desks = no_of_students // 2
    else:
        desks = (no_of_students // 2) + 1
   
    total_desks += desks


print(f"The smallest possible number of desks to be purchased is: {total_desks}")


#  Q. No.16  
students = int(input("Enter the number of students: "))
apples = int(input("Enter the number of apples: "))

apples_distributed = 0
apples_remaining = apples

for i in range(students):
    if apples_remaining > 0:
        apples_distributed += 1
        apples_remaining -= 1

apples_per_student = apples // students
apples_left = apples % students

print(f"Each student gets {apples_per_student} apples.")
print(f"The number of apples remaining in the basket is {apples_left}.")


#  Q. No.17  
age = int(input("Please enter you age"))
if(age>=18):
    print("You are eligibe to vote")
else:
    print("You are not eligible to vote")

#  Q. No.18  
city_monument = {'Delhi':'Red Fort', 'Agra':'Taj Mahal','Jaipur':'Jal Mahal'}
city = input("Enter the name of city (Delhi/Agra/Jaipur) to display the monument of that city")
if (city in city_monument):
    result = city_monument[city]
    print(result)
else:
    print("The city is not in database")

#  Q. No.19  
while True:
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)
        if number % 2 == 0 and number % 3 == 0:
            print(f"{number} is divisible by both 2 and 3.")
            break
        else:
            print(f"{number} is NOT divisible by both 2 and 3. Enter again.")
    except ValueError:
        print("Invalid input! Enter a valid number.")



#  Q. No.20  
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+ - * / % ** //): ")
if(op== '+'):
    print(f"Your answer is: {num1 + num2}")
elif(op== '-'):
    print(num1 - num2)
elif(op== '*'):
    print(f"Your answer is: {num1 * num2}")
elif(op== '/'):
    print(f"Your answer is: {num1 / num2}")
elif(op== '%'):
    print(f"Your answer is {num1 % num2}")
elif(op== '**'):
    print(f"Your answer is {num1 ** num2}")
elif(op== '//'):
    print(f"Your answer is {num1 // num2}")
else:
    print("Please enter valid operator")

#  Q. No.21  
total = int(input("Enter total number of days "))
absent = int(input("Enter toal number of days absent "))
percentage = ((total-absent)/total)*100
if(percentage < 75):
    print("You are ineligible to sit in exam")
else:
    print("You are eligible to sit in exam")
    

#  Q. No.22  
try:
    percentage = float(input("Enter percentage: "))
    if percentage < 40:
        print("Failed")
    elif 40 <= percentage < 55:
        print("Fair")
    elif 55 <= percentage < 65:
        print("Good")
    elif percentage >= 65:
        print("Excellent")
    else:
        print("Invalid percentage.")
except ValueError:
    print("Invalid input! Please enter number.")


#  Q. No.23  
age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ")
days = int(input("Enter number of days: "))

if 18 <= age < 30:
    if gender == 'M':
        wage_per_day = 700
    elif gender == 'F':
        wage_per_day = 750
    else:
        print("Invalid gender.")
else:
    if 30 <= age <= 40:
        if gender == 'M':
            wage_per_day = 800
        elif gender == 'F':
            wage_per_day = 850
        else:
            print("Invalid gender.")
    else:
        print("Age not eligible for wages.")
        wage_per_day = None

if wage_per_day is not None:
    total_wages = wage_per_day * days
    print(f"Total wages: {total_wages}")


#  Q. No.24  
a=True 
b=True 
c=True 
d=True 
print(c)   #True
print(d)   #True
print(not a) #False
print(not b) #False
print(not c) #False
print(not d) #False
print(a and b) #True
print(a or b) #True
print(a and b or c)#True 
print(not a or b or c) #True
print(not a or not b or not c) #False 
print(not(not a or not b or not c)) #True

#  Q. No.25  
a = int(input("Enter first number: "))

if(a % 5 == 0 and a % 3 == 0):
    print("FizzBuzz")
elif(a % 5 == 0):
    print("Buzz")
elif(a % 3 == 0):
    print("Fizz")
else:
    print(a)


#  Q. No.26  
username = 'admin'
password = 'password123'
username_entry = input("Enter username")
password_entry = input("Enter password")
if(username == username_entry and password == password_entry):
    print("Accesss Granted")
else:
    print("Access Denied")

#  Q. No.27  
num1 = float(input("Enter first number "))
num2 = float(input("Enter second number"))

if( num1 > num2):
    print(f"{num1} is greater")
elif (num1 == num2):
    if(num1 > 0):
        print(f"{num1} is positive")
    elif(num1 == 0):
        print(f"{num1} is zero")
    else:
        print(f"{num1} is negative")
else:
    print(f"{num2} is greater")


#  Q. No.28  
subject_score = float(input("Enter subject score"))
if (subject_score > 90):
    print("Congratulations !!!")
elif(50 <= subject_score <= 90):
    print("Satisfactory. You need to work on improving")
else:
    print("Please retake the test.")

#  Q. No.29  
age = int(input("Enter your age: "))
has_degree = input("Do you have a degree? (Y/N): ")

if age >= 18:
    if has_degree == 'Y':
        work_experience = int(input("Enter your years of work experience: "))

        if work_experience > 3:
            print("Highly Eligible.")
        elif 1 <= work_experience <= 3:
            print("Eligible.")
        else:
            print("Under Review.")
    else:
        print("You must have a degree.")
else:
    print("You must be at least 18 years old to be eligible.")


#  Q. No.30  
weight = float(input("Enter the weight of the package (in kg): "))
urgent = input("Is the delivery urgent? (yes/no): ")

if weight < 5:
    cost = 5
elif 5 <= weight <= 20:
    cost = 10
else:
    cost = 15

if urgent == 'yes':
    cost += 5

print(f"The total delivery cost is: ${cost}")


#  Q. No.31  
income = float(input("Enter your income: "))
credit_score = int(input("Enter your credit score: "))

if income > 50000:
    if credit_score > 700:
        print("Loan approved.")
    elif 600 <= credit_score <= 700:
        print("Loan approved with a higher interest rate.")
    else:
        print("Loan rejected.")
else:
    print("Loan rejected due to low income.")


#  Q. No.32  
weather = input("Enter the weather (sunny/rainy): ")

if weather == "sunny":
    print("You can go for hiking or have a picnic!")
elif weather == "rainy":
    raincoat_or_umbrella = input("Do you have a raincoat or umbrella? (yes/no): ")
    if raincoat_or_umbrella == "yes":
        print("You can go to a nearby mall or museum!")
    else:
        print("It's better to stay home and watch movies.")
else:
    print("Invalid weather input. Please enter 'sunny' or 'rainy'.")


#  Q. No.33  
print("Welcome to the Haunted House")

direction = input("Do you want to go upstairs or downstairs? Type (upstairs/downstairs): ")

if direction == 'downstairs':
    print("Game Over")
elif direction == 'upstairs':
    decision1 = input("Do you want to enter the room or stay outside? Type (enter the room/stay outside): ")
    if decision1 == 'enter the room':
        print("Game Over")
    elif decision1 == 'stay outside':
        creature = input("Choose a creature: ghost, vampire, or werewolf? Type (ghost/vampire/werewolf): ")
        if creature == 'ghost' or creature == 'vampire':
            print("Game Over")
        elif creature == 'werewolf':
            print("You Win")
        else:
            print("Invalid option. Type (ghost/vampire/werewolf)")
    else:
        print("Invalid option. Type (enter the room/stay outside)")
else:
    print("Invalid option. Type (upstairs/downstairs)")


#  Q. No.34  
print("Welcome to the Jungle Adventure")

direction = input("Do you want to go left or right? Type (left/right): ")

if direction == 'right':
    print("Game Over")
elif direction == 'left':
    decision1 = input("Do you want to climb a tree or explore the cave? Type (climb a tree/explore the cave): ")
    if decision1 == 'climb a tree':
        print("Game Over")
    elif decision1 == 'explore the cave':
        animal = input("Choose an animal: bear, tiger, or snake? Type (bear/tiger/snake): ")
        if animal == 'bear' or animal == 'tiger':
            print("Game Over")
        elif animal == 'snake':
            print("You Win")
        else:
            print("Invalid option. Type (bear/tiger/snake)")
    else:
        print("Invalid option. Type (climb a tree/explore the cave)")
else:
    print("Invalid option. Type (left/right)")


#  Q. No.35  
print("Welcome to the Magic Forest")

direction = input("Do you want to go north or south? Type (north/south): ")

if direction == 'south':
    print("Game Over")
elif direction == 'north':
    decision1 = input("Do you want to cross the river or follow the path? Type (cross the river/follow the path): ")
    if decision1 == 'cross the river':
        print("Game Over")
    elif decision1 == 'follow the path':
        creature = input("Choose a creature: fairy, ogre, or elf? Type (fairy/ogre/elf): ")
        if creature == 'ogre' or creature == 'fairy':
            print("Game Over")
        elif creature == 'elf':
            print("You Win")
        else:
            print("Invalid option. Type (fairy/ogre/elf)")
    else:
        print("Invalid option. Type (cross the river/follow the path)")
else:
    print("Invalid option. Type (north/south)")


#  Q. No.36  
print("Welcome to the Space Mission")

destination = input("Do you want to go to the moon or to Mars? Type (to the moon/to Mars): ")

if destination == 'to Mars':
    print("Game Over")
elif destination == 'to the moon':
    decision1 = input("Do you want to land on the surface or stay in orbit? Type (land on the surface/stay in orbit): ")
    if decision1 == 'land on the surface':
        print("Game Over")
    elif decision1 == 'stay in orbit':
        object_choice = input("Choose an object: alien, asteroid, or satellite? Type (alien/asteroid/satellite): ")
        if object_choice == 'alien' or object_choice == 'asteroid':
            print("Game Over")
        elif object_choice == 'satellite':
            print("You Win")
        else:
            print("Invalid option. Type (alien/asteroid/satellite)")
    else:
        print("Invalid option. Type (land on the surface/stay in orbit)")
else:
    print("Invalid option. Type (to the moon/to Mars)")


#  Q. No.37  
print("Welcome to the Pirate Island")

direction = input("Do you want to go left or right? Type (left/right): ")

if direction == 'right':
    print("Game Over")
elif direction == 'left':
    decision1 = input("Do you want to dig for treasure or sail the ship? Type (dig for treasure/sail the ship): ")
    if decision1 == 'dig for treasure':
        print("Game Over")
    elif decision1 == 'sail the ship':
        creature = input("Choose a creature: shark, pirate ship, or mermaid? Type (shark/pirate ship/mermaid): ")
        if creature == 'shark' or creature == 'pirate ship':
            print("Game Over")
        elif creature == 'mermaid':
            print("You Win")
        else:
            print("Invalid option. Type (shark/pirate ship/mermaid)")
    else:
        print("Invalid option. Type (dig for treasure/sail the ship)")
else:
    print("Invalid option. Type (left/right)")







