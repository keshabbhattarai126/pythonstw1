# 3. Write a Python program that continuously prompts the user 
# to input a fruit name. If the input is "apple," the program 
# should print "You got it!" and stop. Otherwise, it should 
# display "Try again" and continue.

while True:
    choice = input("Enter fruit name: ")
    if(choice == 'apple'):
        print("You got it!")
        break
    else:
        print("Try again")
        