print('Welcome to the Wizarding World')
subject = input('Choose a subject (spells/potions): ')
if subject == 'spells':
    spells_action = input('Choose your action (practice magic/compete in duels): ')
    if spells_action == 'practice magic':
        print('You mastered a powerful spell. You Win!')
    elif spells_action == 'compete in duels':
        print('You lost to a rival wizard. Game Over.')
elif subject == 'potions':
    potions_action = input('Choose your task (brew an elixir/create poison): ')
    if potions_action == 'brew an elixir':
        print('You healed a village. You Win!')
    elif potions_action == 'create poison':
        print('Your potion backfired. Game Over.')
