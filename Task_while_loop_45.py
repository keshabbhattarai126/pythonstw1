# Content of week4_1.py
a = 'softwarica'
i = 0
while i < 10:
    print(a)
    i += 1

# Content of week4_10.py
lst = [1, 2, 3, 4]
new_list = []
i = 0
while i < len(lst):
    if lst[i] == 1 or lst[i] == 2 or lst[i] == 4:
        new_list.append(lst[i])
    i += 1
print(new_list)

# Content of week4_11.py
lst = [1, 2, 3, 4]
new_list = []
i = 0
while i < len(lst):
    if i == lst[0]:
        new_list.append(lst[0])
    elif i == lst[1]:
        new_list.append('a')
        new_list.append(i)
    elif i != 0 and i != 1:
        new_list.append(i + 1)
    i += 1
print(new_list)

# Content of week4_12.py
given_list = [1, 2, 3, 4, 5]
even = []
odd = []
i = 0
while i < len(given_list):
    if given_list[i] % 2 == 0:
        even.append(given_list[i])
    else:
        odd.append(given_list[i])
    i += 1
print(f"even list is {even}")
print(f"odd list is {odd}")

# Content of week4_13.py
newlist = [1, 2, 3, "d", 4, 5, 'a']
i = 0
while i < len(newlist):
    if isinstance(newlist[i], int):
        print(newlist[i], " is an Integer")
    elif isinstance(newlist[i], str):
        print(newlist[i], " is a String")
    i += 1

# Content of week4_14.py
newlist = [1, 2, 3, "d", 4, 5, 'a']
num, char = [], []
i = 0
while i < len(newlist):
    if isinstance(newlist[i], int):
        num.append(newlist[i])
    elif isinstance(newlist[i], str):
        char.append(newlist[i])
    i += 1
print("The numbers are: ", num, "The Strings are: ", char)

# Content of week4_15.py
user_input = input("Enter a long sentence with numbers: ")
number_of_space = number_of_digits = number_of_letters = 0
i = 0
while i < len(user_input):
    if str(user_input[i]).isspace():
        number_of_space += 1
    elif str(user_input[i]).isdigit():
        number_of_digits += 1
    elif isinstance(user_input[i], str):
        number_of_letters += 1
    i += 1
else:
    print(
        "The number of digits: ", number_of_digits,
        "The number of letters: ", number_of_letters,
        "The number of spaces: ", number_of_space
    )

# Content of week4_16.py
print("Welcome to Mobile Banking")
uname = input('Enter a username: ')
password = input("Enter a password: ")
i = 3
while i > 0:
    username = input("Enter your username: ")
    passkey = input("Enter your password: ")
    if (
        uname != username
        or passkey != password
        or username == ''
        or passkey == ''
    ):
        i -= 1
        if i == 0:
            continue
        print(f"Wrong Username or Password, {i} attempts left.")
    else:
        print("Successful Login")
        break
else:
    print("You are blocked")

# Content of week4_17.py
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is even.")
else:
    print(number, "is odd.")

# Content of week4_18.py
number = int(input("Enter a number: "))
fact = 1
i = 1
while i <= number:
    fact *= i
    i += 1
print("The factorial for ", number, " is ", fact)

# Content of week4_19.py
i = 1
while i < 9:
    j = 1
    while j < 11:
        print(i, "*", j, "=", i * j)
        j += 1
    print("\n")
    i += 1

# Content of week4_2.py
a = [1, 3, 4, 5, 7, 9]
sum = 0
i = 0
while i < len(a):
    sum += a[i]
    i += 1
print("The sum is: ", sum)

# Content of week4_20.py
allist = [1, 2, 3, 4]
i = 0
while i < len(allist):
    if allist[i] == 3:
        break
    print(allist[i])
    i += 1

# Content of week4_21.py
number = int(input("Enter a number: "))
sum_of_odd = 0
i = 0
while i <= number:
    if i % 2 != 0:
        sum_of_odd += i
    i += 1
print("The sum of odd numbers is: ", sum_of_odd)

# Content of week4_22.py
number = int(input("Enter a number: "))
sum_of_even = 0
i = 0
while i <= number:
    if i % 2 == 0:
        sum_of_even += i
    i += 1
print("The sum of even numbers is: ", sum_of_even)

# Content of week4_23.py
user_input = input("Enter long string with a lot of spaces: ")
no_of_spaces = 0
i = 0
while i < len(user_input):
    if str(user_input[i]).isspace():
        no_of_spaces += 1
    i += 1
print("Total no of spaces are: ", no_of_spaces)

# Content of week4_24.py
a = [1, 2, 3, 4]
cube = []
i = 0
while i < len(a):
    cube.append(a[i] ** 3)
    i += 1
print(cube)

# Content of week4_25.py
a = 'programming'
reversed_a = ''
i = len(a) - 1
while i >= 0:
    reversed_a += a[i]
    i -= 1
print(reversed_a)

# Content of week4_26.py
i = 0
while i < 50:
    if i > 7:
        break
    print(i)
    i += 1

# Content of week4_27.py
user_input = input("Enter a string: ")
i = 0
while i < len(user_input):
    print(user_input[i])
    i += 1

# Content of week4_28.py
names = ["Bivek", "Keshab", "Samriddha", "Aayush", "Ishan", "Samuel"]
i = 0
while i < len(names):
    print("Hello!", names[i])
    i += 1

# Content of week4_29.py
names = ["Bivek", "Keshab", "Samriddha", "Aayush", "Ishan", "Samuel", "Mukesh"]
new_names = []
i = 0
while i < len(names):
    new_names.append("Dr." + names[i])
    i += 1
print(new_names)

# Content of week4_3.py
user_input = input("Enter any string")
i = 0
while i < len(user_input):
    print(user_input[i])
    i += 1

# Content of week4_30.py
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square = []
i = 0
while i < len(number):
    square.append(number[i] * number[i])
    i += 1
print(square)

# Content of week4_31.py
lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
newlist = []
i = 0
while i < len(lst1):
    if lst1[i] >= 0:
        newlist.append(lst1[i])
    i += 1
print(newlist)

# Content of week4_32.py
given_list = [0, 1, 2, 3, 4, 5, 6]
i = 0
while i < len(given_list):
    if given_list[i] == 3 or given_list[i] == 6:
        i += 1
        continue
    print(given_list[i])
    i += 1

# Content of week4_33.py
lists, datatype = [], []
user_input = int(input("How many variables would you add: "))
i = 0
while i < user_input:
    new_var = input(f"Enter {i + 1} variable(float, string, int, dict.etc.): ")
    lists.append(new_var)
    i += 1

i = 0
while i < len(lists):
    datatype.append(type(lists[i]))
    i += 1
print(datatype)

# Content of week4_34.py
i = 0
while i <= 10:
    print(i)
    i += 1
else:
    print('Done')

# Content of week4_35.py
i = 105
while i > 0:
    if i < 7:
        break
    print(i)
    i -= 7

# Content of week4_36.py
bad_chars = [';', ':', '!', "*", " "]
string = "py;th* o:n ! ;py * t*h:o !n"
newstring = ''
i = 0
while i < len(string):
    j = 0
    while j < len(bad_chars):
        if string[i] == bad_chars[j]:
            break
        j += 1
    else:
        newstring += string[i]
    i += 1
print(newstring)

# Content of week4_37.py
numbers = []
user_input = int(input("How many numbers would you add: "))
i = 0
while i < user_input:
    new_var = input(f"Enter {i + 1} Number: ")
    numbers.append(new_var)
    i += 1

even = odd = 0
j = 0
while j < len(numbers):
    if int(numbers[j]) % 2 == 0:
        even += 1
    else:
        odd += 1
    j += 1

print("Total even no are:", even, ",and odd no. are:", odd)

# Content of week4_38.py
sum = 0
i = 3
while i < 100:
    if i % 3 == 0 or i % 5 == 0:
        sum += i
    i += 1
print('Sum is: ', sum)

# Content of week4_39.py
sum_of_odd = 0
sum_of_even = 0
i = 1
while i <= 100:
    if i % 2 != 0:
        sum_of_odd += i
    else:
        sum_of_even += i
    i += 1
print("The sum of odd numbers is: ", sum_of_odd)
print("The sum of even numbers is: ", sum_of_even)

# Content of week4_4.py
my_list = [1, "a", "c", 2, 3, 4]
i = 0
while i < len(my_list):
    if isinstance(my_list[i], int):
        print(my_list[i])
    i += 1

# Content of week4_40.py
number = input("Enter a large number: ")
reversenumber = ''
i = len(number) - 1
while i >= 0:
    reversenumber += number[i]
    i -= 1
if number == reversenumber:
    print(number, " is Palindrome.")
else:
    print(number, "is not a Palindrome number.")

# Content of week4_41.py
number = input("Enter a number: ")
armnum = 0
i = 0
while i < len(number):
    armnum += int(number[i]) ** len(number)
    i += 1
if int(number) == armnum:
    print(number, " is Armstrong Number.")
else:
    print(number, "is not a Armstrong number.")

# Content of week4_42.py
user_input = input("Enter a long string: ")
vowel = ['a', 'e', 'i', 'o', 'u']
newstring = ''
i = 0
while i < len(user_input):
    j = 0
    while j < len(vowel):
        if user_input[i] == vowel[j]:
            break
        j += 1
    else:
        newstring += user_input[i]
    i += 1
print(newstring)

# Content of week4_43.py
number = int(input("Enter a number: "))
perfect_num = 0
i = 1
while i < number:
    if number % i == 0:
        perfect_num += i
    i += 1

if perfect_num == number:
    print(number, " is a Perfect number.")
else:
    print(number, " is not a Perfect number.")

# Content of week4_44.py
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
c = []
i = 0
while i < len(a):
    j = 0
    while j < len(b):
        if a[i] == b[j]:
            c.append(a[i])
        j += 1
    i += 1
print("The common elements are: ", c)

# Content of week4_45.py
number = int(input("Enter a number: "))
count = 0
i = 1
while i <= number:
    if number % i == 0:
        count += 1
    if count > 2:
        break
    i += 1
if count == 2:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")

# Content of week4_5.py
my_list = [4, 5, 3, 2]
product = 1
i = 0
while i < len(my_list):
    product *= my_list[i]
    i += 1
print(product)

# Content of week4_6.py
num = int(input("Enter a number to print multiplication table"))
i = 1
while i <= 10:
    print(f'{num} x {i} = {num * i}')
    i += 1

# Content of week4_7.py
my_list = ['a', 3, 'i', 0, 'u']
i = len(my_list) - 1
while i >= 0:
    print(my_list[i])
    i -= 1

# Content of week4_8.py
given_list = [1, 2, 3, 4]
new_list = []
i = 0
while i < len(given_list):
    new_list.append(given_list[i] + 1)
    i += 1
print(new_list)

# Content of week4_9.py
lst = [1, 2, 3, 4]
new_list = []
i = 0
while i < len(lst):
    if lst[i] == 1 or lst[i] == 4:
        new_list.append(lst[i])
    i += 1
print(new_list)
