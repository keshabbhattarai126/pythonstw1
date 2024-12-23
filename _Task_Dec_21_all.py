#Task submitted by Keshab Bhattarai. 37B AI

#Q. No. 1 
price = float(input("Enter price: "))
if (price > 10000):
    discount = price * 0.1
elif (price > 500):
    descount = price * 0.05
print("Final price is: ",price - discount)

#Q. No. 2 
choice = input("Choose vegeterain or non-vegeterian. Enter(veg/nonveg)")
if ( choice == 'veg'):
    order = input("Do you want Salad or Pasta. Enter (salad/pasta)")
    print(f'Your order has been placed for {order}')
elif ( choice == 'nonveg'):
    order = input("Do you want Chicken or Fish. Enter (chicken/fish)")
    print(f'Your order has been placed for {order}')

#Q. No. 3 
salary = float(input("Enter salary amount"))
if (salary < 50000):
    comment = 'high earner'
elif (20000 <= salary <= 50000):
    comment = 'mid earner'
elif ( salary < 20000):
    comment = 'low eaner'


#Q. No. 4 
num = int(input("Enter any integer number: "))
if (num % 2 == 0):
    print(f"{num} is divisible by 2.")
    if (num % 5 == 0):
        print(f'{num} is divisible by 5')
    else:
        print (f'{num} is not divisible by 5')
else:
    print(f'{num} is not divisible by 2')

#Q. No. 5 
marks = float(input("Enter you marks"))
if (marks >= 50):
    if (marks > 90):
        print("Excellent")
    elif ( 51 <= marks <= 90):
        print("Good")
else:
    print("Fail")


#Q. No. 6 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 > num2:
    if num1 > num3:
        greatest = num1
    else:
        greatest = num3
else:
    if num2 > num3:
        greatest = num2
    else:
        greatest = num3

print(f'{greatest} is the greatest number.')


#Q. No. 7 
print('Welcome to Forest Adventure')
direction = input("Choose the path (left/right) ")
if (direction == 'left'):
    action = input('Pick the option (explore/left)')
    if (action == 'explore'):
        print('You found treasure!')
    elif (action == 'rest'):
        print('You were attacked by wild animals. Game Over! ')
elif (direction == 'right'):
    print('You were attacked by wild animals.Game Over! ')

#Q. No. 8 
print('Welcome to the Jungle Survival Challenge')
choice = input('Choose your action (search for food/build a shelter): ')
if choice == 'search for food':
    method = input('Choose your method (hunt/gather): ')
    if method == 'hunt':
        print('You were attacked by a wild animal. Game Over.')
    elif method == 'gather':
        print('You found enough food. You Win!')
elif choice == 'build a shelter':
    print('Your shelter collapsed in the rain. Game Over.')


#Q. No. 9 
print('Welcome to the Space Adventure')
destination = input('Choose your destination (land on Mars/fly to Jupiter): ')
if destination == 'land on Mars':
    action = input('Choose your action (explore/build a base): ')
    if action == 'explore':
        print('You found alien artifacts. You Win!')
    elif action == 'build a base':
        print('You ran out of resources. Game Over.')
elif destination == 'fly to Jupiter':
    print('Your spaceship crashed. Game Over.')


#Q. No. 10 
print('Welcome to the Haunted Castle')
decision = input('Choose your action (enter the castle/run away): ')
if decision == 'enter the castle':
    door = input('Choose a door (red/green/black): ')
    if door == 'red':
        print('You entered a room full of flames. Game Over.')
    elif door == 'green':
        print('You found the treasure. You Win!')
    elif door == 'black':
        print('You were captured by ghosts. Game Over.')
elif decision == 'run away':
    print('You escaped safely.')


#Q. No. 11 
print('Welcome to the Underwater World')
action = input('Choose your action (dive deeper/surface): ')
if action == 'dive deeper':
    task = input('Choose your task (search for pearls/chase the fish): ')
    if task == 'search for pearls':
        print('You found a rare pearl. You Win!')
    elif task == 'chase the fish':
        print('You got lost underwater. Game Over.')
elif action == 'surface':
    print('You returned safely.')


#Q. No. 12 
print('Welcome to the Pirate Ship Adventure')
adventure = input('Choose your adventure (search for treasure/battle enemy ships): ')
if adventure == 'search for treasure':
    treasure_action = input('Choose your action (dig on the island/explore the cave): ')
    if treasure_action == 'dig on the island':
        print('You found a hidden treasure chest. You Win!')
    elif treasure_action == 'explore the cave':
        print('You were trapped inside. Game Over.')
elif adventure == 'battle enemy ships':
    battle_action = input('Choose your strategy (attack/defend): ')
    if battle_action == 'attack':
        print('You won the battle. You Win!')
    elif battle_action == 'defend':
        print('You were outnumbered. Game Over.')


#Q. No. 13 
print('Welcome to the Wizarding World')
subject = input('Choose a subject (spells/potions): ')
if subject == 'spells':
    spells_action = input('Choose your action (practice magic/compete in duels): ')
    if spells_action == 'practice magic':
        print('You mastered a powerful spell. You Win!')
    elif spells_action == 'compete in duels':
        print('You lost to a rival wizard. Game Over.')
elif subject == 'potions':
    potions_action = input('Choose your task (brew an elixir/create poison): ')
    if potions_action == 'brew an elixir':
        print('You healed a village. You Win!')
    elif potions_action == 'create poison':
        print('Your potion backfired. Game Over.')


#Q. No. 14 
print('Welcome to the Cybersecurity Mission')
mission = input('Choose your mission (trace the hacker/secure the system): ')
if mission == 'trace the hacker':
    trace_action = input('Choose your strategy (track their IP/decode their message): ')
    if trace_action == 'track their IP':
        print('You caught the hacker. You Win!')
    elif trace_action == 'decode their message':
        print('The message was a trap. Game Over.')
elif mission == 'secure the system':
    secure_action = input('Choose your method (shut down the server/upgrade the firewall): ')
    if secure_action == 'shut down the server':
        print('The attack was stopped. You Win!')
    elif secure_action == 'upgrade the firewall':
        print('The hacker bypassed it. Game Over.')


#Q. No. 15 
num = int(input("Enter a number"))
if ( num % 2 == 0 and num % 7 == 0):
    print("Double Seven")
elif ( num % 2 == 0 and num % 7 != 0):
    print("ैEven")
elif (num % 7 == 0 and num % 2 != 0):
    print("Lucky Seven")
else:
    print(num)

#Q. No. 16 
num = input("Enter a number")
if (num > 100):
    print("Big Number")
elif( 50 <= num <= 100):
    print ("Medium Number")
elif(num < 50):
    print("Small Number")
    

#Q. No. 17 
color = input("Enter a color: ")
if color == "Red":
    print("Stop")
elif color == "Yellow":
    print("Slow Down")
elif color == "Green":
    print("Go")
else:
    print("Invalid Signal")


#Q. No. 18 
temperature = int(input("Enter temperature in Celsius: "))
if temperature > 40:
    print("Hot")
elif 20 <= temperature <= 39:
    print("Warm")
elif temperature < 20:
    print("Cold")


#Q. No. 19 
bmi = float(input("Enter your BMI value: "))
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal weight")
elif 25 <= bmi < 29.9:
    print("Overweight")
elif bmi >= 30:
    print("Obesity")





#Q. No. 20 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Sum:", num1 + num2)
elif (num1 % 2 == 0 and num2 % 2 != 0) or (num1 % 2 != 0 and num2 % 2 == 0):
    print("Difference:", abs(num1 - num2))
else:
    print("Product:", num1 * num2)


#Q. No. 21 
price = float(input("Enter the price of the item: "))
if price > 1000:
    discount = price * 0.20
    print("New Price:", price - discount)
elif 500 <= price <= 1000:
    discount = price * 0.10
    print("New Price:", price - discount)
elif price < 500:
    print("No discount. Price:", price)


#Q. No. 22 
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

#Q. No. 23 
age = int(input("Enter age: "))
gender = input("Enter gender (m/f): ")
score = int(input("Enter academic score (out of 100): "))

if 18 <= age <= 25:
    if gender == 'm':
        if score >= 85:
            print("Full Scholarship")
        elif score >= 70:
            print("Partial Scholarship")
        else:
            print("No Scholarship")
    elif gender == 'f':
        if score >= 80:
            print("Full Scholarship")
        elif score >= 65:
            print("Partial Scholarship")
        else:
            print("No Scholarship")


#Q. No. 24 
age = int(input("Enter age: "))
gender = input("Enter gender (m/f): ")
experience = int(input("Enter years of experience: "))

if 21 <= age <= 35:
    if gender == 'm':
        if experience >= 5:
            print("Senior Developer")
        else:
            print("Junior Developer")
    elif gender == 'f':
        if experience >= 5:
            print("Senior Analyst")
        else:
            print("Junior Analyst")
elif age > 35:
    print("Manager Role")


#Q. No. 25 
age = int(input("Enter age: "))
gender = input("Enter gender (m/f): ")
show_type = input("Enter show type (Matinee/Evening): ")

if age < 12:
    if show_type == "Matinee":
        ticket = 500
    elif show_type == "Evening":
        ticket = 700
elif 12 <= age < 60:
    if gender == 'm':
        if show_type == "Matinee":
            ticket = 800
        elif show_type == "Evening":
            ticket = 1000
    elif gender == 'f':
        if show_type == "Matinee":
            ticket = 700
        elif show_type == "Evening":
            ticket = 900
elif age >= 60:
    ticket = 600

print(f"Ticket Price: Rs{ticket}")


#Q. No. 26 
age = int(input("Enter age: "))
gender = input("Enter gender (m/f): ")
membership = input("Enter membership type (Monthly/Yearly): ")

if 18 <= age < 30:
    if gender == 'm':
        if membership == "Monthly":
            price = 50
        elif membership == "Yearly":
            price = 500
    elif gender == 'f':
        if membership == "Monthly":
            price = 45
        elif membership == "Yearly":
            price = 450
elif 30 <= age <= 50:
    if membership == "Monthly":
        price = 60
    elif membership == "Yearly":
        price = 600
elif age > 50:
    if membership == "Monthly":
        price = 40
    elif membership == "Yearly":
        price = 400

print(f"Membership Price: Rs{price}")




