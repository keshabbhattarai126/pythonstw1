newlist = [1, 2, 3, "d", 4, 5, 'a']
num, char = [], []
i = 0
while i < len(newlist):
    if isinstance(newlist[i], int):
        num.append(newlist[i])
    elif isinstance(newlist[i], str):
        char.append(newlist[i])
    i += 1
print("The numbers are: ", num, "The Strings are: ", char)

