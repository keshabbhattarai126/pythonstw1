odd=[]
even=[]
for i in range(1,21):
    if(i % 2 == 0):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)