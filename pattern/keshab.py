
for row in range(7):
    for column in range(33):
        if (column == 0):
            print("*", end=" ")
        elif (column ==1) and (row == 2 or row == 4):
            print("*", end=" ")
        elif(column ==2) and (row == 1 or row == 5):
            print("*", end=" ")
        elif(column ==3) and (row == 0 or row == 6):
            print("*", end=" ")


        elif(column == 4 or column == 5):
            print(" ", end=" ")
        elif(column == 6) :
            print("*", end=" ")
        elif(column == 7 or column == 8 or column == 9) and (row == 0 or row==3 or row==6):
            print("*", end=" ")

        elif(column == 10 or column==11):
            print(" ", end=" ")
        elif column == 12 and (row==1 or row == 2):
             print("*", end=" ")
        elif (column == 13 or column == 14) and (row == 0 or row == 3 or row == 6):
            print("*", end=" ")
        elif column == 15 and (row==4 or row == 5):
             print("*", end=" ")

        elif(column == 16 or column== 17):
            print(" ", end=" ")
        elif(column == 18 or column == 21 ):
            print("*",end=" ")
        elif(column == 19 or column == 20) and row == 3:
            print("*", end=" ")

        elif(column == 21 or column== 22):
            print(" ", end=" ")
        elif (column == 23 or column ==27) and row !=0 :
            print("*", end=" ")
        elif (column==24 or column==25 or column==26) and (row==0 or row==3):
            print("*", end=" ")
        

        elif(column == 27 or column== 28):
            print(" ", end=" ")
        elif(column == 29):
            print("*",end=" ")
        elif(column == 30 or column == 31) and (row == 0 or row == 3 or row == 6):
            print("*", end=" ")
        elif(column == 32) and (row != 0 and row != 6):
            print("*", end= " ")
            
        else:
            print(end="  ")
    
    print()