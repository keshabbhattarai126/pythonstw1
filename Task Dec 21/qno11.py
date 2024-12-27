print('Welcome to the Underwater World')
action = input('Choose your action (dive deeper/surface): ')
if action == 'dive deeper':
    task = input('Choose your task (search for pearls/chase the fish): ')
    if task == 'search for pearls':
        print('You found a rare pearl. You Win!')
    elif task == 'chase the fish':
        print('You got lost underwater. Game Over.')
elif action == 'surface':
    print('You returned safely.')
