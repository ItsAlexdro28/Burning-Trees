import random

width = 1
state = {}

# generate matrix
def Grid(width):
    grid = []
    for i in range(width):
        row = []
        for j in range(width):
            row.append("*")
        grid.append(row)

    if (width % 2) == 0:
        m = width/2
        middle = int(m)
        grid[middle][middle] = "@"
    else:
        m = width/2 - 0.5
        middle = int(m)
        grid[middle][middle] = "@"
    return grid
            
# turns matrix onto a dictionary with cordinates
def Scan(matrix, state):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            key = str(i) + "," + str(j)
            value = matrix[i][j]
            state[key] = value
    return state

# generates a Tick that uses the given probability of burning neighbor trees and applyes the changes
def Tick(matrix, probability, state):
    burning = {}
    for f, v in state.items():
        if v == "@":
            burning[f] = v

    for f, v in burning.items():
        raw = f.split(",")
        rawCordinate = [int(raw[0]),int(raw[1])]
        targetX = rawCordinate[0]
        targetY = rawCordinate[1]
        hit = 0

        # upper tree
        targetX = rawCordinate[0] - 1
        hit = random.randint(1, 100)
        if hit <= probability and matrix[targetX][targetY] == "*":
            matrix[targetX][targetY] = "@"

        # down tree
        targetX = rawCordinate[0] + 1
        hit = random.randint(1, 100)
        if hit <= probability and matrix[targetX][targetY] == "*":
            matrix[targetX][targetY] = "@"

        targetX = rawCordinate[0]

        # left tree
        targetY = rawCordinate[1] - 1
        hit = random.randint(1, 100)
        if hit <= probability and matrix[targetX][targetY] == "*":
            matrix[targetX][targetY] = "@"

        # right tree
        targetY = rawCordinate[1] + 1
        hit = random.randint(1, 100)
        if hit <= probability and matrix[targetX][targetY] == "*":
            matrix[targetX][targetY] = "@"

        matrix[rawCordinate[0]][rawCordinate[1]] = "~"

    return(matrix)



#main fuction
def main():
    width = input("n length:")
    matrix = Grid(int(width))
    stateNow = Scan(matrix, state)

    #print nice matrix fucntion
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix]))

    #count number of values
    ceros = sum(1 for v in stateNow.values() if v == "*")
    unos = sum(1 for v in stateNow.values() if v == "@")
    dos = sum(1 for v in stateNow.values() if v == "~")
    print(ceros)
    print(unos)
    print(dos)

    print("\n")

    probability = int(input("Probability of fire spreading (1 - 100): "))
    while True:
        print("\n")
        matrix = Tick(matrix, probability, stateNow)
        print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix]))
        print("\n")
        stateNow = Scan(matrix, state)
        ceros = sum(1 for v in stateNow.values() if v == "*")
        unos = sum(1 for v in stateNow.values() if v == "@")
        dos = sum(1 for v in stateNow.values() if v == "~")
        print(f"Number of live trees: {ceros}")
        print(f"Number of burning trees: {unos}")
        print(f"Number of dead trees: {dos}")
        x = input("next tick?")
    # ask N rows
    # generate grid
    # ask probability
    # make time line menu

if __name__ == "__main__":
    main()

