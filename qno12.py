print('Welcome to the Pirate Ship Adventure')
adventure = input('Choose your adventure (search for treasure/battle enemy ships): ')
if adventure == 'search for treasure':
    treasure_action = input('Choose your action (dig on the island/explore the cave): ')
    if treasure_action == 'dig on the island':
        print('You found a hidden treasure chest. You Win!')
    elif treasure_action == 'explore the cave':
        print('You were trapped inside. Game Over.')
elif adventure == 'battle enemy ships':
    battle_action = input('Choose your strategy (attack/defend): ')
    if battle_action == 'attack':
        print('You won the battle. You Win!')
    elif battle_action == 'defend':
        print('You were outnumbered. Game Over.')
