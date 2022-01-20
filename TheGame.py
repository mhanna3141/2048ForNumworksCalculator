from kandinsky import *


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
    startx = 10
    starty = 10
    squareDims = 30
    extraSpace = 3
    for i in range(gameGridDim):
        for j in range(gameGridDim):

            fill_rect(startx + j * (squareDims + extraSpace),
                      starty + i * (squareDims + extraSpace),
                      squareDims,
                      squareDims,
                      colorDict[gameGrid[i][j]])


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
    [2, None, None, None],
    [4, 4, 8, 4],
    [16, None, 2, None]
]
drawSquares()
tk.mainloop()