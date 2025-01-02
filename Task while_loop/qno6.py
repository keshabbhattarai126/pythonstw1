# 6. Write a Python program that generates a random number 
# between 1 and 10 and prompts the user to guess the number. 
# The program should provide hints such as "guess higher" or 
# "guess lower" based on the user's input. Once the user guesses
# the correct number, the program should display the number of 
# attempts it took to guess the correct number.

import random
a = random.randint(1,10)
i = 1
while True:
    
    rand_a = int(input("Enter first number: "))
    if(rand_a == a):
        print(i,'attempts')
        break
    elif(rand_a>a):
        print("gusess lower")
    elif(rand_a<a):
        print("guess higher")
    i = i + 1


    