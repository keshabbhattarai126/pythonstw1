user_input = input("Enter long string with a lot of spaces: ")
no_of_spaces = 0
i = 0
while i < len(user_input):
    if str(user_input[i]).isspace():
        no_of_spaces += 1
    i += 1
print("Total no of spaces are: ", no_of_spaces)

