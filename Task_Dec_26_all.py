# Content of week4_1.py
a = 'softwarica'
for i in range(10):
    print(a)

# Content of week4_10.py
lst = [1,2,3,4]
new_list = []
for i in lst:
    if i == 1 or i == 2 or i == 4:
        new_list.append(i)
print(new_list)

# Content of week4_11.py
lst = [1, 2, 3, 4]
new_list = []

for i in range(len(lst)):
    if i == lst[0]:
        new_list.append(lst[0])
    elif i == lst[1]:
        new_list.append('a')
        new_list.append(i)
    elif i != 0 and i != 1:
        new_list.append(i+1)

print(new_list)
    
   

# Content of week4_12.py
given_list = [1,2,3,4,5]
even =[]
odd=[]
for i in given_list:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(f"even list is {even}")
print(f"odd list is {odd}")

# Content of week4_13.py
newlist = [1,2,3,"d",4,5,'a']
num, char = [],[]
for i in newlist:
    if isinstance(i,int):
        print(i," is an Integer")
    elif isinstance(i,str):
        print(i," is a String")

# Content of week4_14.py
newlist = [1,2,3,"d",4,5,'a']
num, char = [],[]
for i in newlist:
    if isinstance(i,int):
        num.append(i)
    elif isinstance(i,str):
        char.append(i)
print(
    "The numbers are: ",num,
    "The Strings are: ",char
)

# Content of week4_15.py
user_input = input("Enter a long sentences with numbers: ")
number_of_space = number_of_digits = number_of_letters = 0
for i in user_input:
    if str(i).isspace():
        number_of_space += 1
    elif str(i).isdigit():
        number_of_digits += 1
    elif isinstance(i,str):
        number_of_letters += 1
else:
    print(
        "The number of digits: ",number_of_digits,
        "The number of letters: ",number_of_letters,
        "The number of spaces: ",number_of_space
    )

# Content of week4_16.py
print("Welcome to Mobile Banking")
uname = input('Enter a username: ')
password = input("Enter a password: ")

for i in range(3,0,-1):
    username = input("Enter your username: ")
    passkey = input("Enter your password: ")
    if (
        uname != username
        or passkey != password
        or username == ''
        or passkey == ''
    ):
        if i == 1:
            continue
        print(f"Wrong Username or Password, {i-1} attempts left.")
    else:
        print("Successful Login")
        break
else:
    print("You are blocked")

# Content of week4_17.py
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number,"is even.")
else:
    print(number,"is odd.")

# Content of week4_18.py

number = int(input("Enter a number: "))
fact = 1
for i in range(1,number+1):
    fact *= i
print("The factorial for ",number," is ",fact)


# Content of week4_19.py

for i in range(1,9):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)
    print("\n")


# Content of week4_2.py
a = [1,3,4,5,7,9]
sum = 0
for i in range (len(a)):
    sum = sum + a[i]
print("The sum is: ",sum)

# Content of week4_20.py
allist = [1,2,3,4]
for i in allist:
    if i == 3:
        break;
    print(i)

# Content of week4_21.py
number = int(input("Enter a number: "))
sum_of_odd = 0
for i in range(number+1):
    if i % 2 != 0:
        sum_of_odd += i
print("The sum of odd numbers is: ",sum_of_odd)

# Content of week4_22.py
number = int(input("Enter a number: "))
sum_of_even = 0
for i in range(number+1):
    if i % 2 == 0:
        sum_of_even += i
print("The sum of even numbers is: ",sum_of_even)

# Content of week4_23.py
user_input = input("Enter long string with a lot of spaces: ")
no_of_spaces = 0
for i in user_input:
    if str(i).isspace():
        no_of_spaces += 1
print("Total no of spaces are: ",no_of_spaces)

# Content of week4_24.py
a = [1,2,3,4]
cube = []
for i in a:
    cube.append(i**3)
print(cube)

# Content of week4_25.py
a = 'programming'
reversed_a = ''
for i in range(len(a)-1,-1,-1):
    reversed_a += a[i]
print(reversed_a)

# Content of week4_26.py
for i in range(50):
    if i > 7:
        break
    print(i)

# Content of week4_27.py
user_input = input("Enter a string: ")
for i in user_input:
    print(i)

# Content of week4_28.py
names = ["Bivek","Keshab","Samriddha","Aayush","Ishan","Samuel"]
for name in names:
    print("Hello!",name)

# Content of week4_29.py
names = ["Bivek","Keshab","Samriddha","Aayush","Ishan","Samuel","Mukesh"]
new_names = []
for name in names:
    new_names.append("Dr."+name)
print(new_names)

# Content of week4_3.py
user_input= input(("Enter any string"))
for i in user_input:
    print(i)

# Content of week4_30.py
number = [1,2,3,4,5,6,7,8,9,10]
square = []
for i in number:
    square.append(i*i)
print(square)

# Content of week4_31.py
lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
newlist = []
for i in lst1:
    if i >= 0:
        newlist.append(i)
print(newlist)

# Content of week4_32.py
given_list = [0,1,2,3,4,5,6]
for i in given_list:
    if i == 3 or i == 6:
        continue
    print(i)

# Content of week4_33.py

lists,datatype = [],[]
user_input = int(input("How many variables would you add: "))
for i in range(user_input):
    new_var = input(f"Enter {i+1} variable(float, string, int, dict.etc.): ")
    lists.append(new_var)

for data in lists:
    datatype.append(type(data))
print(datatype)


# Content of week4_34.py
for i in range(11):
    print(i)
else:
    print('Done')

# Content of week4_35.py
for i in range(105,0,-7):
    if i < 7:
        break
    print(i)

# Content of week4_36.py
bad_chars = [';', ':', '!', "*", " "]
string = "py;th* o:n ! ;py * t*h:o !n"
newstring = ''

for i in string:
    for j in bad_chars:
        if i == j:
            break
    else:
        newstring += i

            
print(newstring)

# Content of week4_37.py
numbers = []
user_input = int(input("How many numbers would you add: "))
for i in range(user_input):
    new_var = input(f"Enter {i+1} Number: ")
    numbers.append(new_var)

even = odd = 0
for number in numbers:
    if int(number) % 2 == 0:
        even += 1
    else:
        odd += 1

print("Total even no are:",even,",and odd no. are:",odd)

# Content of week4_38.py
sum = 0
for i in range(3,100):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print('Sum is: ',sum)

# Content of week4_39.py
sum_of_odd = 0
sum_of_even = 0
for i in range(1,101):
    if i % 2 != 0:
        sum_of_odd += i
    else:
        sum_of_even += i
print("The sum of odd numbers is: ",sum_of_odd)
print("The sum of even numbers is: ",sum_of_even)

# Content of week4_4.py
my_list=[1,"a","c",2,3,4]

for i in my_list:
    if isinstance(i,int):
     print(i)
    



# Content of week4_40.py
number = input("Enter a large number: ")
reversenumber = ''
for i in range(len(number)-1,-1,-1):
    reversenumber += number[i]
# print(reversenumber)
if number == reversenumber:
    print(number," is Palindrome.")
else:
    print(number,"is not a Palindrome number.")

# Content of week4_41.py
number = input("Enter a number: ")
armnum = 0
for i in range(len(number)):
    # print(i)
    armnum += int(number[i])**len(number)
# print(armnum)
if int(number) == armnum:
    print(number," is Armstrong Number.")
else:
    print(number,"is not a Armstrong number.")

# Content of week4_42.py
user_input = input("Enter a long string: ")
vowel = ['a','e','i','o','u']
newstring = ''
for i in user_input:
    for v in vowel:
        if i == v:
            break
    else:
        newstring += i
print(newstring)

# Content of week4_43.py
number = int(input("Enter a number: "))
perfect_num = 0

for i in range(1,number):
    if number % i == 0:
        perfect_num += i

if perfect_num == number:
    print(number," is a Perfect number.")
else:
    print(number," is not a Perfect number.")

# Content of week4_44.py
a = [1,2,3,4,5]
b = [3,4,5,6,7]
c = []

for i in a:
    for j in b:
        if i == j:
            c.append(i)

print("The common elements are: ",c)

# Content of week4_45.py
number = int(input("Enter a number: "))
count = 0
for i in range(1,number+1):
    if number % i == 0:
        count += 1
    if count > 2:
        break
if count == 2:
    print(number,"is a prime number.")
else:
    print(number,"is not a prime number.")

# Content of week4_5.py
my_list = [4,5,3,2]
product = 1

for i in my_list:
    product = product * i

print(product)

# Content of week4_6.py
num = int(input("Enter a number to print multiplication table"))
for i in range(1,11):
    print(f'{num} x {i} = {num*i}')

# Content of week4_7.py
my_list = ['a',3,'i',0,'u']
for i in range (len(my_list)-1,-1,-1):
    print(my_list[i])


# Content of week4_8.py
given_list = [1, 2, 3, 4]
new_list = []

for i in range(len(given_list)):
    new_list.append(given_list[i] + 1)

print(new_list)


# Content of week4_9.py
lst = [1,2,3,4]
new_list = []
for i in lst:
    if i == 1 or i == 4:
        new_list.append(i)
print(new_list)

