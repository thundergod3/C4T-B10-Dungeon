player = {
    "x": 2,
    "y": 2
}

escape = {
    "x": 2,
    "y": 3
}

key = {
    "x": 4,
    "y": 4
}

flag = False

while True:
    for i in range(4):
        for j in range(4):
            if (i == player['y'] - 1) and (j == player['x'] - 1):
                print("P", end=" ")
            elif (i == escape['y'] - 1) and (j == escape['x'] - 1):
                print("E", end=" ")
            elif (i == key['y'] - 1) and (j == key['x'] - 1):
                if flag == False:
                    print("K", end=" ")
                else:
                    print("-", end=" ")
            else:
                print("-", end=" ")
        print()

    move = input("A S D W ? ")

    

    if move == "w":
        player['y'] -= 1
        if player["y"] == 0:
            print("Out of move !!!!") 
            player['y'] += 1 
    if move == "s":
        player['y'] += 1
        if player["y"] > 4:
            print("Out of move !!!!") 
            player['y'] -= 1
    if move == "a":
        player['x'] -= 1
        if player["x"] == 0:
            print("Out of move !!!!") 
            player['x'] += 1 
    if move == "d":
        player['x'] += 1
        if player["x"] > 4:
            print("Out of move !!!!") 
            player['x'] -= 1 

    if (player['x'] == key['x']) and (player['y'] == key['y']):
        print("Found key !!!!")
        flag = True
    
    if (player['x'] == escape['x']) and (player['y'] == escape['y']): 
        if flag == False:
            print("Need key !!!")
        else:
            print("You won !!!!")
            for i in range(4):
                for j in range(4):
                    if (i == player['y'] - 1) and (j == player['x'] - 1):
                        print("P", end=" ")
                    elif (i == escape['y'] - 1) and (j == escape['x'] - 1):
                        print("E", end=" ")
                    elif (i == key['y'] - 1) and (j == key['x'] - 1):
                        if flag == False:
                            print("K", end=" ")
                        else:
                            print("-", end=" ")
                    else:
                        print("-", end=" ")
                print()
            
            break
            