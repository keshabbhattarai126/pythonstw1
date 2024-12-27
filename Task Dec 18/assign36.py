print("Welcome to the Space Mission")

destination = input("Do you want to go to the moon or to Mars? Type (to the moon/to Mars): ")

if destination == 'to Mars':
    print("Game Over")
elif destination == 'to the moon':
    decision1 = input("Do you want to land on the surface or stay in orbit? Type (land on the surface/stay in orbit): ")
    if decision1 == 'land on the surface':
        print("Game Over")
    elif decision1 == 'stay in orbit':
        object_choice = input("Choose an object: alien, asteroid, or satellite? Type (alien/asteroid/satellite): ")
        if object_choice == 'alien' or object_choice == 'asteroid':
            print("Game Over")
        elif object_choice == 'satellite':
            print("You Win")
        else:
            print("Invalid option. Type (alien/asteroid/satellite)")
    else:
        print("Invalid option. Type (land on the surface/stay in orbit)")
else:
    print("Invalid option. Type (to the moon/to Mars)")
