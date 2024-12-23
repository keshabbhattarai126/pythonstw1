price = float(input("Enter the price of the item: "))
if price > 1000:
    discount = price * 0.20
    print("New Price:", price - discount)
elif 500 <= price <= 1000:
    discount = price * 0.10
    print("New Price:", price - discount)
elif price < 500:
    print("No discount. Price:", price)
