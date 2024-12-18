print("Welcome to the Magic Forest")

direction = input("Do you want to go north or south? Type (north/south): ")

if direction == 'south':
    print("Game Over")
elif direction == 'north':
    decision1 = input("Do you want to cross the river or follow the path? Type (cross the river/follow the path): ")
    if decision1 == 'cross the river':
        print("Game Over")
    elif decision1 == 'follow the path':
        creature = input("Choose a creature: fairy, ogre, or elf? Type (fairy/ogre/elf): ")
        if creature == 'ogre' or creature == 'fairy':
            print("Game Over")
        elif creature == 'elf':
            print("You Win")
        else:
            print("Invalid option. Type (fairy/ogre/elf)")
    else:
        print("Invalid option. Type (cross the river/follow the path)")
else:
    print("Invalid option. Type (north/south)")
