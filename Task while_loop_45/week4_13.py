newlist = [1, 2, 3, "d", 4, 5, 'a']
i = 0
while i < len(newlist):
    if isinstance(newlist[i], int):
        print(newlist[i], " is an Integer")
    elif isinstance(newlist[i], str):
        print(newlist[i], " is a String")
    i += 1

