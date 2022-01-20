

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


gameGridDim = 4

gameGrid = [
    [None, None, 2, 2],
    [2, None, None, None],
    [4, 4, 8, 4],
    [16, None, 2, None]
]

print(shiftListRight([2, 2, 2, 2]))
print()
for row in gameGrid:
    print(row)
shiftGameGrid("UP")
print()
for row in gameGrid:
    print(row)