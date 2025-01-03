lst = [1, 2, 3, 4]
new_list = []
i = 0
while i < len(lst):
    if i == lst[0]:
        new_list.append(lst[0])
    elif i == lst[1]:
        new_list.append('a')
        new_list.append(i)
    elif i != 0 and i != 1:
        new_list.append(i + 1)
    i += 1
print(new_list)

