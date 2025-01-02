
for row in range(7):
    for column in range(40):
        if (column == 0):
            print("*", end=" ")
        elif (column ==1) and (row == 2 or row == 4):
            print("*", end=" ")
        elif(column ==2) and (row == 1 or row == 5):
            print("*", end=" ")
        elif(column ==3) and (row == 0 or row == 6):
            print("*", end=" ")
        else:
            print(end="  ")
    
    print()