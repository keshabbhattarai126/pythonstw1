Pizza = '$10'
Burger = '7'
Pasta = '8'

option = (input("Enter item name (Pizza/Burger/Pasta) to know its price"))
option = option.upper()
if(option == 'PIZZA'):
    print(f"The price of Pizza is {Pizza}")
elif(option == 'BURGER'):
    print(f"The price of Burger is {Burger}")
elif(option == 'PASTA'):
    print(f"The price of Pasta is {Pasta}")
else:
    print("Invalid Item")
