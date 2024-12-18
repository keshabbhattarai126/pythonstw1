while True:
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)
        if number % 2 == 0 and number % 3 == 0:
            print(f"{number} is divisible by both 2 and 3.")
            break
        else:
            print(f"{number} is NOT divisible by both 2 and 3. Enter again.")
    except ValueError:
        print("Invalid input! Enter a valid number.")
