given_list = [1,2,3,4,5]
even =[]
odd=[]
for i in given_list:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(f"even list is {even}")
print(f"odd list is {odd}")