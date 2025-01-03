user_input = input("Enter a long string: ")
vowel = ['a', 'e', 'i', 'o', 'u']
newstring = ''
i = 0
while i < len(user_input):
    j = 0
    while j < len(vowel):
        if user_input[i] == vowel[j]:
            break
        j += 1
    else:
        newstring += user_input[i]
    i += 1
print(newstring)

