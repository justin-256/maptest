"""
MAP INTERACTION TEST 3.1
Use n s e w to move, open/close to open and close the gate, and L+/-N to add or remove light level of area
"""

lightdict = {
    "1,1":1,
    "3,1":1,
    "3,2":1,
    "3,3":1,
    "2,3":1,
    "1,3":1,
    "1,2":1 
}

gate = False

def updatemap():
    global map
    map = {
    "0,0":False, "1,0":False, "2,0":False, "3,0":False, "4,0":False, 
    "0,1":False, "1,1":True,  "2,1":gate,  "3,1":True,  "4,1":False, 
    "0,2":False, "1,2":True,  "2,2":False, "3,2":True,  "4,2":False,
    "0,3":False, "1,3":True,  "2,3":True,  "3,3":True,  "4,3":False,
    "0,4":False, "1,4":False, "2,4":False, "3,4":False, "4,4":False,
    }

updatemap()

currentloc = [1,1]
while True:
    skiplocs = ["2,1"]
    gateloc = "2,1"
    x = 0
    y = 0
    max_x = 4
    max_y = 4
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
    print("GATE OPENED: " + str(map[gateloc]))
    print("LIGHT LEVEL: " + str(lightdict[','.join(str(e) for e in currentloc)]))
    move = input("> ")
    
    if move == "n":
        x = currentloc.copy()
        x[1] = x[1]-1
        if map[",".join(str(i) for i in x)] == True:
            print("Going north")
            currentloc = x
            if ','.join(str(e) for e in currentloc) in skiplocs:
               currentloc[1] = currentloc[1]-1
        elif map[",".join(str(i) for i in x)] == False:
            print("You cant go there!")
        else:
            print("ERROR")
            
    if move == "s":
        x = currentloc.copy()
        x[1] = x[1]+1
        if map[",".join(str(i) for i in x)] == True:
            print("Going south")
            currentloc = x
            if ','.join(str(e) for e in currentloc) in skiplocs:
               currentloc[1] = currentloc[1]+1
        elif map[",".join(str(i) for i in x)] == False:
            print("You cant go there!")
        else:
            print("ERROR")
            
    if move == "e":
        x = currentloc.copy()
        x[0] = x[0]+1
        if map[",".join(str(i) for i in x)] == True:
            print("Going east")
            currentloc = x
            if ','.join(str(e) for e in currentloc) in skiplocs:
               currentloc[0] = currentloc[0]+1
        elif map[",".join(str(i) for i in x)] == False:
            print("You cant go there!")
        else:
            print("ERROR")
            
    if move == "w":
        x = currentloc.copy()
        x[0] = x[0]-1
        if map[",".join(str(i) for i in x)] == True:
            print("Going west")
            currentloc = x
            if ','.join(str(e) for e in currentloc) in skiplocs:
               currentloc[0] = currentloc[0]-1
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
        
    move = list(move)
    if move[0] == "L":
        if move[1] == "+":
            lightdict[','.join(str(e) for e in currentloc)] += int(move[2])
        if move[1] == "-":
            lightdict[','.join(str(e) for e in currentloc)] -= int(move[2])
    
"""
CHANGELOG:
ver1: no map
ver2: added map
ver3: added skippable locations
ver3.1: expanded map
ver4: Added light! 
"""
