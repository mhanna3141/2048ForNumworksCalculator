

def shiftListRight(givenList):

    # loop through list
    for i in range(2):
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
def shiftGameGrid(xDirection, yDirection):
    pass


gameGridDim = 4

gameGrid = [
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None]
]

print(shiftListRight([2, 2, 2, 2]))