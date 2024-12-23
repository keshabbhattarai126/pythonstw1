print('Welcome to the Haunted Castle')
decision = input('Choose your action (enter the castle/run away): ')
if decision == 'enter the castle':
    door = input('Choose a door (red/green/black): ')
    if door == 'red':
        print('You entered a room full of flames. Game Over.')
    elif door == 'green':
        print('You found the treasure. You Win!')
    elif door == 'black':
        print('You were captured by ghosts. Game Over.')
elif decision == 'run away':
    print('You escaped safely.')
