# Write a Python program that takes a character input and checks whether it is a vowel or consonant.

vowels = {'a', 'e', 'i', 'o', 'u'}
uppercase_vowels = {letter.upper() for letter in vowels}

letter = input("Enter any alphabet (a to z): ")

if len(letter) == 1 and letter.isalpha():

    if letter in vowels or letter in uppercase_vowels:
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is a consonant")
else:
    print("Invalid. Please enter a single alphabet character.")
