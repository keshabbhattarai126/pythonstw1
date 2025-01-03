my_list = [1, "a", "c", 2, 3, 4]
i = 0
while i < len(my_list):
    if isinstance(my_list[i], int):
        print(my_list[i])
    i += 1

