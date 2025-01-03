bad_chars = [';', ':', '!', "*", " "]
string = "py;th* o:n ! ;py * t*h:o !n"
newstring = ''
i = 0
while i < len(string):
    j = 0
    while j < len(bad_chars):
        if string[i] == bad_chars[j]:
            break
        j += 1
    else:
        newstring += string[i]
    i += 1
print(newstring)

