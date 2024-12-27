print("Welcome to the Haunted House")

direction = input("Do you want to go upstairs or downstairs? Type (upstairs/downstairs): ")

if direction == 'downstairs':
    print("Game Over")
elif direction == 'upstairs':
    decision1 = input("Do you want to enter the room or stay outside? Type (enter the room/stay outside): ")
    if decision1 == 'enter the room':
        print("Game Over")
    elif decision1 == 'stay outside':
        creature = input("Choose a creature: ghost, vampire, or werewolf? Type (ghost/vampire/werewolf): ")
        if creature == 'ghost' or creature == 'vampire':
            print("Game Over")
        elif creature == 'werewolf':
            print("You Win")
        else:
            print("Invalid option. Type (ghost/vampire/werewolf)")
    else:
        print("Invalid option. Type (enter the room/stay outside)")
else:
    print("Invalid option. Type (upstairs/downstairs)")
