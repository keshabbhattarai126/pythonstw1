sample_list = [12,13,14,15,16,17,18,19]
length = len(sample_list)
odd = []
for i in range(length):
    if sample_list[i] % 2 == 1:
        odd.append(sample_list[i])
print(odd)