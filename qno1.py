price = float(input("Enter price: "))
if (price > 10000):
    discount = price * 0.1
elif (price > 500):
    descount = price * 0.05
print("Final price is: ",price - discount)