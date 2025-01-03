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

