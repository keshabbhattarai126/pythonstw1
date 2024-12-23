choice = input("Choose vegeterain or non-vegeterian. Enter(veg/nonveg)")
if ( choice == 'veg'):
    order = input("Do you want Salad or Pasta. Enter (salad/pasta)")
    print(f'Your order has been placed for {order}')
elif ( choice == 'nonveg'):
    order = input("Do you want Chicken or Fish. Enter (chicken/fish)")
    print(f'Your order has been placed for {order}')
