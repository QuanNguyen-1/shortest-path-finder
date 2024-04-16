import random

#moving the object
def left(x,y):
    x -= 1
    return [x, y]

def right(x,y):
    x += 1
    return [x, y]

def up(x,y):
    y += 1
    return [x, y]

def down(x,y):
    y -= 1
    return [x, y]

#calculating the G,H,F values
def calcG(currentx, currenty, startx, starty):
    diffx = abs(currentx-startx)
    diffy = abs(currenty-starty)
    return diffx + diffy

def calcH(currentx, currenty, finalx, finaly):
    diffx = abs(currentx-finalx)
    diffy = abs(currenty-finaly)
    return diffx + diffy

def calcF(G,F):
    return G+F

def clear():
    result = []
    open_dic = {}
    current_open_list = []
    lowF = float('inf')
    chosen_square = []
    g_values = {}
    f_list = []
    g_list = []

def main():
    #ask user for the width and height of the board
    width = int(input("How many tiles wide is the board? "))
    height = int(input("How many tiles high is the board? "))

    board = []

    for x in range(1,width+1):
        for y in range(1,height+1):
            board.append((x,y))

    print("board:")
    print(board)


    #ask user for starting point
    while True:
        startx = int(input("Starting x position? "))
        if startx < 0 or startx > width:
            print("input is not within 0 and "+str(width))
            continue
        else:
            break

    while True:
        starty = int(input("Starting y position? "))
        if starty < 0 or starty > height:
            print("input is not within 0 and "+str(height))
            continue
        else:
            break



    #ask user for end point
    while True:
        finalx = int(input("Final x position? "))
        if finalx < 0 or finalx > width:
            print("input is not within 0 and "+str(width))
            continue
        else:
            break

    while True:
        finaly = int(input("Final y position? "))
        if finaly < 0 or finaly > height:
            print("input is not within 0 and "+str(height))
            continue
        else:
            break


    #pick 3 squares randomly to be obstacles except for the start and end points
    obstacle_list = [] 

    for i in board:
        if i != (startx,starty) and i != (finalx,finaly):
            obstacle_list.append(i)
    obstacles = random.choices(obstacle_list, k=3)


    print("The obstacles are:")
    print(obstacles)

    #starting point and ending point
    start = ((startx, starty))
    final = ((finalx, finaly))
    #actual current position and test position
    (currentx, currenty) = start
    #(testx,testy) = start
    current = ((currentx, currenty))


    lowF = float('inf') #G+H

    #closed and open lists
    open_list = [] #keeps track of all open squares
    current_open_list = [] #keeps track of the current open squares for the current square
    open_dic = {} #keeps track of f value for squares in open list, key = square, value = f value
    closed_list = [] #already vistied squares
    path_dic = {} #keeps track of parent square of other squares, key = square, value = parent square
    path = [] #track of squares from start to end
    result = [] #feasible squares that can be obtained from current square
    final_path = [] #final path
    g_values = {} #keeps track of h values, key = square, value = h value
    g_list = [] #h values of the squares with the lowest f values
    f_list = [] #squares with the lowest f value
    key = ((finalx,finaly))






    #loop keeps going until we reach final square
    while current != final:
        x1,y1 = up(currentx,currenty)
        x2,y2 = left(currentx,currenty)
        x3,y3 = right(currentx,currenty)
        x4,y4 = down(currentx,currenty)

        result.append((x1,y1))
        result.append((x2,y2))
        result.append((x3,y3))
        result.append((x4,y4))

    #adding neighbors to open list if possible (not out of bounds or visited already or obstacle)
        for x,y in result:
            if x <= width and x > 0 and y <= height and y > 0 and (x,y) not in closed_list and (x,y) not in obstacles:
                current_open_list.append((x,y))
            else:
                pass

    #add to open list
        for i in current_open_list:
            open_list.append(i)

    #if open list has squares from closed list, remove
        for x,y in open_list:
            if (x,y) in closed_list:
                open_list.remove((x,y))



    #calculates the F score for each square in open list, if same f choose most recent square
        for x,y in open_list:
            G = calcG(x,y,startx,starty)
            H = calcH(x,y,finalx,finaly)
            F = calcF(G,H)
            open_dic[(x,y)] = F
            g_values[(x,y)] = G
            lowF = min(lowF,F)

    #path - adjacent square attached to parent square, key = child; parent = value
        for i in current_open_list:
            path_dic[i] = ((currentx,currenty))

    #add current square to closed list
        closed_list.append((currentx,currenty))

    #square with lowest F score becomes the current square
        for key, value in open_dic.items():
            if value == lowF:
                f_list.append(key)
        
        for i in f_list:
            g_list.append(g_values[i])

        chosen_square = [i for i in g_values if g_values[i] == min(g_list)]
        current = chosen_square[-1] #most recent square added to open list if all H and F the same
        currentx,currenty = current




    #clear out result and open_dic and current open list
    clear()

    #get path by looking at the parent squares starting with the final square
    path.append((finalx,finaly))
    while key in path_dic:
        path.append(path_dic[key])
        key = path_dic[key]

    #return the path 
    path.reverse()
    final_path = str(path)
    print("The shortest path is: " + final_path.replace("),",") ->"))

main()



