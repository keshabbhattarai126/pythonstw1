sample_list = [3, 7, 2, 8, 5]
largest_num = 0
for i in range(len(sample_list)):
    if sample_list[i] > largest_num:
        largest_num = sample_list[i]
print(f"The largest number is {largest_num}")