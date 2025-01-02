# 4. Create a Python program that asks the user to guess the password.
#  The program should keep asking until the user enters "open sesame."
#  For each incorrect guess, print "Wrong password, try again." 
# When the correct password is entered, print "Access granted!"

while True:
    choice = input("Guess the password")
    if(choice == 'open sesame'):
        print("Access Granted!")
        break
    else:
        print("Wrong Password")
        