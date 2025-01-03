given_list = [0, 1, 2, 3, 4, 5, 6]
i = 0
while i < len(given_list):
    if given_list[i] == 3 or given_list[i] == 6:
        i += 1
        continue
    print(given_list[i])
    i += 1

