print("Welcome to the Pirate Island")

direction = input("Do you want to go left or right? Type (left/right): ")

if direction == 'right':
    print("Game Over")
elif direction == 'left':
    decision1 = input("Do you want to dig for treasure or sail the ship? Type (dig for treasure/sail the ship): ")
    if decision1 == 'dig for treasure':
        print("Game Over")
    elif decision1 == 'sail the ship':
        creature = input("Choose a creature: shark, pirate ship, or mermaid? Type (shark/pirate ship/mermaid): ")
        if creature == 'shark' or creature == 'pirate ship':
            print("Game Over")
        elif creature == 'mermaid':
            print("You Win")
        else:
            print("Invalid option. Type (shark/pirate ship/mermaid)")
    else:
        print("Invalid option. Type (dig for treasure/sail the ship)")
else:
    print("Invalid option. Type (left/right)")
