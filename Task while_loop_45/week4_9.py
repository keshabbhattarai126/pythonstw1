lst = [1, 2, 3, 4]
new_list = []
i = 0
while i < len(lst):
    if lst[i] == 1 or lst[i] == 4:
        new_list.append(lst[i])
    i += 1
print(new_list)
