from kandinsky import *
from random import randint, choice
from ion import *


def shiftListRight(givenList):

    # loop through list
    for itemIndex in range(len(givenList)):

        # item is None or no where to move item
        if givenList[itemIndex] is None or itemIndex == gameGridDim-1:
            continue

        else:

            # can combined current index and next index
            if givenList[itemIndex] == givenList[itemIndex+1]:
                givenList[itemIndex + 1] = givenList[itemIndex] * 2
                del givenList[itemIndex]
                givenList.insert(0, None)

            # just move current index to the right
            elif givenList[itemIndex + 1] is None:
                del givenList[itemIndex + 1]
                givenList.insert(0, None)

    return givenList


#
def shiftGameGrid(direction):

    # merge right
    if direction == "RIGHT":

        # loop through rows
        for rowIndex in range(len(gameGrid)):

            gameGrid[rowIndex] = shiftListRight(gameGrid[rowIndex])

    # merge left
    elif direction == "LEFT":

        # loop through rows
        for rowIndex in range(len(gameGrid)):
            sendList = gameGrid[rowIndex]
            sendList.reverse()
            sendList = shiftListRight(sendList)
            sendList.reverse()
            gameGrid[rowIndex] = sendList

    elif direction == "DOWN":

        for columnIndex in range(len(gameGrid[0])):

            sendList = []

            # loop through rows
            for row in gameGrid:

                sendList.append(row[columnIndex])

            sendList = shiftListRight(sendList)

            for rowIndex in range(len(sendList)):
                gameGrid[rowIndex][columnIndex] = sendList[rowIndex]

    else:

        for columnIndex in range(len(gameGrid[0])):

            sendList = []

            # loop through rows
            for row in gameGrid:
                sendList.append(row[columnIndex])

            sendList.reverse()
            sendList = shiftListRight(sendList)
            sendList.reverse()

            for rowIndex in range(len(sendList)):
                gameGrid[rowIndex][columnIndex] = sendList[rowIndex]


def drawSquares():

    extraSpace = 3
    startx = 50
    starty = 10
    squareDims = 50

    for i in range(gameGridDim):
        for j in range(gameGridDim):

            fill_rect(startx + j * (squareDims + extraSpace),
                      starty + i * (squareDims + extraSpace),
                      squareDims,
                      squareDims,
                      colorDict[gameGrid[i][j]])


def addRandomTile():

    emptyLocations = getNoneTileCords()

    # space for a new tile
    if emptyLocations:
        if randint(1, 10) < 10:
            tile = 4
        else:
            tile = 2

        selectedSpot = choice(emptyLocations)
        gameGrid[selectedSpot[0]][selectedSpot[1]] = tile


# returns a list full of where the empty tiles are
def getNoneTileCords():
    locations = []
    for rowIndex in range(len(gameGrid)):
        for columnIndex in range(len(gameGrid[rowIndex])):
            if gameGrid[rowIndex][columnIndex] is None:
                locations.append((rowIndex, columnIndex))
    return locations


def startGame():
    left = False
    right = False
    down = False
    up = False
    while True:
        if keydown(KEY_LEFT):
            left = True
        elif keydown(KEY_RIGHT):
            right = True
        elif keydown(KEY_UP):
            up = True
        elif keydown(KEY_DOWN):
            down = True

        if not keydown(KEY_LEFT) and left:
            shiftGameGrid("LEFT")
            addRandomTile()
            drawSquares()
            left = False
        elif not keydown(KEY_RIGHT) and right:
            shiftGameGrid("RIGHT")
            addRandomTile()
            drawSquares()
            right = False
        elif not keydown(KEY_UP) and up:
            shiftGameGrid("UP")
            addRandomTile()
            drawSquares()
            down = False
        elif not keydown(KEY_DOWN) and down:
            shiftGameGrid("DOWN")
            addRandomTile()
            drawSquares()
            up = False


colorDict = {
    None: (204, 192, 179),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
    4094: (0, 0, 0)
}

gameGridDim = 4

gameGrid = [
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None]
]

addRandomTile()
addRandomTile()
drawSquares()

while True:
    movementCheck()