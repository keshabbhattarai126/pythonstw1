floor = ['floor1','floor2','floor3']
room = [1,2,3]
for i in floor:
    for j in room:
        if i == 'floor2':
            if j==1 or j==3:
                continue
            else:
                print(j)
        elif i == 'floor3':
            if j == 1 or j==2:
                continue
            else:
                print(j)
        else:
            print(j)

