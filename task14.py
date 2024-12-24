string = input("Enter string value: ")
for i in range(len(string)):
    if i % 2 == 1:
        print(f'{string[i]}',end = '')
