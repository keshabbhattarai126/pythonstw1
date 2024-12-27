print("Welcome to the Treasure Land")

direction = input("Enter direction (left/right)")

if direction == 'right':
    print("Game Over")
elif direction == 'left':
    decision1= input("Do you want to swim or wait? Type(swim/wait)")
    if(decision1 == 'swim'):
        print("Game Over")
    elif decision1 == 'wait':
        color = input("Choose a color? (blue/red/yellow)")
        if(color == 'blue' or color == 'red'):
            print("Game Over")
        elif(color == 'yellow'):
            print("You win")
        else:
            print("Invalid Option. Type (red/blue/yellow)")
    else:
        print("Invalid option. Type(swim/wait)")
else:
    print("Invalid option. Type (left/right)")

