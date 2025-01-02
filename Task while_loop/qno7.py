# 7. Write a Python program that simulates a login system. The program 
# should prompt the user to enter a username and password. If both are 
# correct (e.g., username is "admin" and password is "1234"), 
# print "Login successful" and exit. If either is incorrect, 
# print "Invalid credentials, try again." Allow the user up to 
# 3 attempts before locking them out with the message "Too many failed attempts."

username = "admin"
password = "1234"
attempts = 3

while attempts > 0:
    username_input = input("Enter username: ")
    password_input = input("Enter password: ")
    
    if username_input == username and password_input == password:
        print("Login successful")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Invalid credentials, {attempts} attempt(s) left.")
        else:
            print("Too many failed attempts. Account locked.")
