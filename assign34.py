print("Welcome to the Jungle Adventure")

direction = input("Do you want to go left or right? Type (left/right): ")

if direction == 'right':
    print("Game Over")
elif direction == 'left':
    decision1 = input("Do you want to climb a tree or explore the cave? Type (climb a tree/explore the cave): ")
    if decision1 == 'climb a tree':
        print("Game Over")
    elif decision1 == 'explore the cave':
        animal = input("Choose an animal: bear, tiger, or snake? Type (bear/tiger/snake): ")
        if animal == 'bear' or animal == 'tiger':
            print("Game Over")
        elif animal == 'snake':
            print("You Win")
        else:
            print("Invalid option. Type (bear/tiger/snake)")
    else:
        print("Invalid option. Type (climb a tree/explore the cave)")
else:
    print("Invalid option. Type (left/right)")
