given_list = [1, 2, 3, 4, 5]
even = []
odd = []
i = 0
while i < len(given_list):
    if given_list[i] % 2 == 0:
        even.append(given_list[i])
    else:
        odd.append(given_list[i])
    i += 1
print(f"even list is {even}")
print(f"odd list is {odd}")

