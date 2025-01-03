lists, datatype = [], []
user_input = int(input("How many variables would you add: "))
i = 0
while i < user_input:
    new_var = input(f"Enter {i + 1} variable(float, string, int, dict.etc.): ")
    lists.append(new_var)
    i += 1

i = 0
while i < len(lists):
    datatype.append(type(lists[i]))
    i += 1
print(datatype)

