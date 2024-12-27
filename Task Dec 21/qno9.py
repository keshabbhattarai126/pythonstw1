print('Welcome to the Space Adventure')
destination = input('Choose your destination (land on Mars/fly to Jupiter): ')
if destination == 'land on Mars':
    action = input('Choose your action (explore/build a base): ')
    if action == 'explore':
        print('You found alien artifacts. You Win!')
    elif action == 'build a base':
        print('You ran out of resources. Game Over.')
elif destination == 'fly to Jupiter':
    print('Your spaceship crashed. Game Over.')
