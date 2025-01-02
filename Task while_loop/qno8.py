# 8. Write a Python program that simulates a basic arithmetic quiz. 
# Generate two random numbers between 1 and 30 and ask the user to 
# provide the result of their multiplication. If the answer is correct, 
# print "Correct!" and generate a new question. If the answer is wrong, 
# print "Incorrect, try again." Allow the user to stop the quiz when the 
# user enters "exit"

import random

print("Welcome to the Arithmetic Quiz!")
print('Type "exit" anytime to stop the quiz.')

while True:
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    correct_answer = num1 * num2

    user_input = input(f"What is {num1} * {num2}? ")

    if user_input.lower() == "exit":
        print("Quiz ended. Thank you for playing!")
        break

    if user_input.isdigit() and int(user_input) == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect, try again. The correct answer is {correct_answer}.")
