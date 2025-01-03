a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
c = []
i = 0
while i < len(a):
    j = 0
    while j < len(b):
        if a[i] == b[j]:
            c.append(a[i])
        j += 1
    i += 1
print("The common elements are: ", c)

