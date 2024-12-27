#12.Write a Python program to check if a given character is uppercase, lowercase, or a digit.

char = input("Enter a single character: ")


if len(char) != 1:
    print("Enter only one character")
else:
   
    if char.isupper():
        print(f"'{char}' is an uppercase .")
    
    elif char.islower():
        print(f"'{char}' is a lowercase.")
    
    elif char.isdigit():
        print(f"'{char}' is a digit.")
    
    else:
        print(f"'{char}' is a not uppercase, lowercase or digit.")
