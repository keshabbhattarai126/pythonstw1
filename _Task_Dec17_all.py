#Task submitted by Keshab Bhattarai. 37B AI

#1. Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3"

a = int(input("Enter first number"))
b = int(input("Enter second number"))


if a==b:
    print(1)
elif a>b:
    print(2)
else:
    print(3)

#2. Check whether the user input number is even or odd and display it to user

a=int(input("Enter a number"))
if(a%2==0):
	print("The number is even")
else:
	print("The number is odd")
      
#3.
a ={1:'Jan', 2:'feb', 3:'mar', 4:'apr', 5:'may', 6:'june', 7:'july', 8:'augu',9:'sept',10:'oct',11:'nov',12:'dec'}
b=int(input("Enter any no 1 to 12 "))
if b in a:
	result=a[b]
	print(result)
else:
    print("Out of range")

#4.
grade = int(input("Enter marks"))
if(grade<25):
	print("F")
elif(grade>=25 and grade<45):
	print("E")
elif(grade>=45 and grade<50):
	print("D")
elif(grade>=50 and grade<60):
	print("C")
elif(grade>=60 and grade<80):
	print("B")
elif(grade>=80):
	print("A")

#5. Write a program to check whether a number is divisible by 7 or not

num = int(input("Enter a number"))
if(num % 7==0):
    print(f"{num} is divisible by 7")
else:
    print(f"{num} is not divisible by 7")
	
#6. Write a program to accept two numbers and mathematical operators and perform operation accordingly.

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

#7. Write a program to display "Hello" if a number entered by user is a multiple of five, otherwise print "Bye".
num = int(input("Enter a number: "))
if(num % 5 == 0):
    print("Hello")
else:
    print("Bye")

#8. 
a = int(input("Enter first number: "))

if(a % 5 == 0 and a % 3 == 0):
    print("FizzBuzz")
elif(a % 5 == 0):
    print("Buzz")
elif(a % 3 == 0):
    print("Fizz")
else:
    print(a)

#9. Write a Python program that takes a character input and checks whether it is a vowel or consonant.

vowels = {'a', 'e', 'i', 'o', 'u'}
uppercase_vowels = {letter.upper() for letter in vowels}

letter = input("Enter any alphabet (a to z): ")

if len(letter) == 1 and letter.isalpha():

    if letter in vowels or letter in uppercase_vowels:
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is a consonant")
else:
    print("Invalid. Please enter a single alphabet character.")

#10.
mark = int(input("Enter marks"))
if(90 <= mark <= 100):
    print("A")
elif(80 <= mark <= 89):
    print("B")
elif(70 <= mark <= 79):
    print("C")
elif(mark < 70):
    print("Fail")

#11.
age = int(input("Enter age: "))
if(age < 13):
    print ("Child")
elif(13 <= age <= 19):
    print("Teenager")
elif(age>19):
    print("Adult")


#12.Write a Python program to check if a given character is uppercase, lowercase, or a digit.

char = input("Enter a single character: ")


if len(char) != 1:
    print("Enter only one character")
else:
   
    if char.isupper():
        print(f"'{char}' is an uppercase .")
    
    elif char.islower():
        print(f"'{char}' is a lowercase.")
    
    elif char.isdigit():
        print(f"'{char}' is a digit.")
    
    else:
        print(f"'{char}' is a not uppercase, lowercase or digit.")

#13. 
color = input("Enter color")
color = color.upper()
if(color == 'RED'):
    print("Stop")
elif(color == 'YELLOW'):
    print("Get Ready")
elif(color == 'GREEN'):
    print('Go')
else:
    print("Invalid input")

#14.
age = int(input("Enter age"))
experience =int(input("Enter experience in years"))
if(age>18 and experience>=2):
    print("Eligible")
else:
    print("Not eligible")

#15.
temp = float(input("Enter temperature in degree C"))
if(temp > 30):
    print("It's hot,stay hydrated")
elif(15 < temp < 30):
    print("Enjoy the weather!")
elif( temp < 15):
    print("It's cold,wear warm clothers!")

#16.
Pizza = '$10'
Burger = '7'
Pasta = '8'

option = (input("Enter item name (Pizza/Burger/Pasta) to know its price"))
option = option.upper()
if(option == 'PIZZA'):
    print(f"The price of Pizza is {Pizza}")
elif(option == 'BURGER'):
    print(f"The price of Burger is {Burger}")
elif(option == 'PASTA'):
    print(f"The price of Pasta is {Pasta}")
else:
    print("Invalid Item")

#17.
height = float(input("Enter height in feet"))
if(height >= 6):
    print("Selected")
else:
    print("Not Selected")

#18.
age = float(input("Enter your age"))
if(age>=18):
    print("Allowed")
else:
    print("Not Allowed")

#19.
username = 'admin'
password = 'password123'
username_entry = input("Enter username")
password_entry = input("Enter password")
if(username == username_entry and password == password_entry):
    print("Accesss Granted")
else:
    print("Access Denied")

#20.
winter = {1,2,12}
spring = {3,4,5}
summer = { 9,10,11}

try:
    month = int(input("Enter a month number (1–12): "))
    
    
    if month in winter:
        print(f"The season for month {month} is Winter.")
    elif month in spring:
        print(f"The season for month {month} is Spring.")
    elif month in summer:
        print(f"The season for month {month} is Summer.")
    elif month in autumn:
        print(f"The season for month {month} is Autumn.")
    else:
        print("Invalid month. Please enter a number between 1 and 12.")

except ValueError:
    print("Invalid .Enter an integer between 1 and 12.")

#21.
salary = float(input("Enter salary"))
credit_score=float(input("Enter credit score"))
if(salary>=50000 and credit_score>=700):
    print("Eligible")
else:
    print("Not eligible")
    

#22.
num = int(input("Enter a number"))
if(1 <= num <= 100):
    print(f"Yes, the number {num} is between 1 and 100")
else:
    print(f"No,the number {num} doesnot lie between 1 and 100")