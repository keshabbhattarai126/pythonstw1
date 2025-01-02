# 9. Write a Python program that prompts the user to enter a number. 
# The program should determine whether the number is prime or not. 
# If the number is prime, print "The number is prime." Otherwise, print
#  "The number is not prime." Continue prompting the user until they enter "exit."

while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    
    if user_input == "exit":
        print("Program ended.")
        break

    number = int(user_input)
    if number < 2:
        print("The number is not prime.")
        continue

    is_prime = True
    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        print("The number is prime.")
    else:
        print("The number is not prime.")
