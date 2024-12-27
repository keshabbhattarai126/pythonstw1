a ={1:'Jan', 2:'feb', 3:'mar', 4:'apr', 5:'may', 6:'june', 7:'july', 8:'augu',9:'sept',10:'oct',11:'nov',12:'dec'}
b=int(input("Enter any no 1 to 12 "))
if b in a:
	result=a[b]
	print(result)
else:
    print("Out of range")
