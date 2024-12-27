sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
length = len(sample_list)
even = []
for i in range(length):
    if sample_list[i] % 2 == 0:
        even.append(sample_list[i])
print(even)