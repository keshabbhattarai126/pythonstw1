number = input("Enter a large number: ")
reversenumber = ''
i = len(number) - 1
while i >= 0:
    reversenumber += number[i]
    i -= 1
if number == reversenumber:
    print(number, " is Palindrome.")
else:
    print(number, "is not a Palindrome number.")

