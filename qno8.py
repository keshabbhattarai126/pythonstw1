print('Welcome to the Jungle Survival Challenge')
choice = input('Choose your action (search for food/build a shelter): ')
if choice == 'search for food':
    method = input('Choose your method (hunt/gather): ')
    if method == 'hunt':
        print('You were attacked by a wild animal. Game Over.')
    elif method == 'gather':
        print('You found enough food. You Win!')
elif choice == 'build a shelter':
    print('Your shelter collapsed in the rain. Game Over.')
