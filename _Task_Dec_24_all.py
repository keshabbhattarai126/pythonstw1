#Task submitted by Keshab Bhattarai 37B AI

# Q. No. 1
a = [1,2,3,4]
for i in range(len(a)-1,-1,-1):
    print(a[i])


# Q. No. 2
a = 'softwarica'
for i in range(len(a)-1,-1,-1):
    print(a[i])

# Q. No. 3
num = int(input("Enter a number to display multiplication table"))
for i in range(1,11):
    print(num, 'x', i, '=',num*i)

# Q. No. 4
a = ["apple", "banana", "cherry"]
for i in range(len(a)):
   print(a[i])

# Q. No. 5
odd=[]
even=[]
for i in range(1,21):
    if(i % 2 == 0):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

# Q. No. 6,py
for i in range(10,301,10):
    print(i, end=' ')


# Q. No. 7
for i in range(105,6,-7):
    print(i)

# Q. No. 8
num = int(input("Enter number to calculate factorial: "))
fact = 1
for i in range(num, 1, -1):
    fact = fact * i
print(f"The factorial of {num} is {fact}")

# Q. No.  9
num = int(input("Enter number to reverse it: "))

rev_num = 0

for i in range(len(str(num))):
    each_digit = num % 10
    rev_num = rev_num * 10 + each_digit
    num //= 10
print(f"The reverse number is {rev_num}")




# Q. No. 10
myList = "Parameter"
count = 0
for char in myList:
    count += 1
print(f"The number of characters in the string is: {count}")


# Q. No. 11
sample_list = [8,2,3,-1,7]
product = 1 
for i in range (len(sample_list)):
    product = product * sample_list[i]
print(product)

# Q. No. 12
sample_list = [8, 2, 3, 0, 7]
sum = 0
for i in range (len(sample_list)):
    sum = sum + sample_list[i]
print(sum)

# Q. No. 13
string = input("Enter string value: ")
for i in range(len(string)):
    if i % 2 == 0 and i / 2 != 0:
        print(f'{string[i]}',end = '')


# Q. No. 14
string = input("Enter string value: ")
for i in range(len(string)):
    if i % 2 == 1:
        print(f'{string[i]}',end = '')


# Q. No. 15
start = int(input("Enter starting number"))
stop = int(input("Enter stopping number"))
sum = 0
for i in range(start, stop + 1):
    sum = sum + i
print(f"The sum is {sum}")  

# Q. No. 16
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
length = len(sample_list)
even = []
for i in range(length):
    if sample_list[i] % 2 == 0:
        even.append(sample_list[i])
print(even)

# Q. No. 17
sample_list = [12,13,14,15,16,17,18,19]
length = len(sample_list)
odd = []
for i in range(length):
    if sample_list[i] % 2 == 1:
        odd.append(sample_list[i])
print(odd)

# Q. No. 18
for i in range(1 , 101):
    if i % 5 == 0:
        print(i, end = ' ')

# Q. No. 19
sample_list = [3, 7, 2, 8, 5]
largest_num = 0
for i in range(len(sample_list)):
    if sample_list[i] > largest_num:
        largest_num = sample_list[i]
print(f"The largest number is {largest_num}")



# Q. No. 20
for num in range(1, 11):
    print(f"Square of {num} is {num ** 2}")


# Q. No. 21
for num in range(1, 6):
    print(f"Cube of {num} is {num ** 3}")


# Q. No. 22
for char in "Python":
    print(f"Character: {char}")


# Q. No. 23
for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} is divisible by 3 and 5")




