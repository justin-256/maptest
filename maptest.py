"""
MAP INTERACTION TEST 2 (version 1 didn't have the printed map)

Use n s e w to move, and open/close to open and close the gate
its only a prototype and I still want to assign certain spots 
as skippable and check when moving to see if it needs to be 
skipped and repeat the action.
"""
gate = False

def updatemap():
    global map
    map = {
    "0,0":False, "1,0":False, "2,0":False, "3,0":False, "4,0":False, 
    "0,1":False, "1,1":True,  "2,1":gate,  "3,1":True,  "4,1":False, 
    "0,2":False, "1,2":False, "2,2":False, "3,2":False, "4,2":False}

updatemap()

currentloc = [1,1]
while True:
    gateloc = "2,1"
    x = 0
    y = 0
    max_x = 4
    max_y = 2
    while y <= max_y:
        while x <= max_x:
            if ','.join(str(e) for e in currentloc) == str(x)+","+str(y):
                print("X", end="")
            elif gateloc == str(x)+","+str(y) and gate == False:
                print("|", end="")
            elif map[str(x)+","+str(y)] == True:
                print(" ", end="")
            elif map[str(x)+","+str(y)] == False:
                print("#", end="")
            x+=1
            
        y += 1
        x = 0
        print("")

    print("CURRENT LOCATION: " + str(currentloc))
    print("GATE OPENED: " + str(map["1,2"]))
    move = input("Where to move? ")
    if move == "n":
        x = currentloc.copy()
        x[1] = x[1]-1
        if map[",".join(str(i) for i in x)] == True:
            print("Going north")
            currentloc = x
        elif map[",".join(str(i) for i in x)] == False:
            print("You cant go there!")
        else:
            print("ERROR")
    elif move == "s":
        x = currentloc.copy()
        x[1] = x[1]+1
        if map[",".join(str(i) for i in x)] == True:
            print("Going south")
            currentloc = x
        elif map[",".join(str(i) for i in x)] == False:
            print("You cant go there!")
        else:
            print("ERROR")
    elif move == "e":
        x = currentloc.copy()
        x[0] = x[0]+1
        if map[",".join(str(i) for i in x)] == True:
            print("Going east")
            currentloc = x
        elif map[",".join(str(i) for i in x)] == False:
            print("You cant go there!")
        else:
            print("ERROR")
    elif move == "w":
        x = currentloc.copy()
        x[0] = x[0]-1
        if map[",".join(str(i) for i in x)] == True:
            print("Going west")
            currentloc = x
        elif map[",".join(str(i) for i in x)] == False:
            print("You cant go there!")
        else:
            print("ERROR")
    elif move == "open":
        gate = True
        updatemap()    
    elif move == "close":
        gate = False
        updatemap()
