user_input = input("Enter a long sentence with numbers: ")
number_of_space = number_of_digits = number_of_letters = 0
i = 0
while i < len(user_input):
    if str(user_input[i]).isspace():
        number_of_space += 1
    elif str(user_input[i]).isdigit():
        number_of_digits += 1
    elif isinstance(user_input[i], str):
        number_of_letters += 1
    i += 1
else:
    print(
        "The number of digits: ", number_of_digits,
        "The number of letters: ", number_of_letters,
        "The number of spaces: ", number_of_space
    )

