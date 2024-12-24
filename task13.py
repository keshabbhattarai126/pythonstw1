string = input("Enter string value: ")
for i in range(len(string)):
    if i % 2 == 0 and i / 2 != 0:
        print(f'{string[i]}',end = '')
