username = 'user123'
password = 'password123'

username_input = input("Enter username")
password_input = input("Enter passowrd")

i = 3
while(i > 0):
    
    if username_input != username or password_input != password or len(username_input)<8 or username_input == "" or password_input == "":

        print(f'Incorrect username or password. {i} attempt left')
        i = i - 1