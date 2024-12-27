print('Welcome to Forest Adventure')
direction = input("Choose the path (left/right) ")
if (direction == 'left'):
    action = input('Pick the option (explore/left)')
    if (action == 'explore'):
        print('You found treasure!')
    elif (action == 'rest'):
        print('You were attacked by wild animals. Game Over! ')
elif (direction == 'right'):
    print('You were attacked by wild animals.Game Over! ')