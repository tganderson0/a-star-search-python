import math


# G is the movement cost from the start point A to the current square
# H is the estimated movement cost from the current square to the destination
# Coordinates are in the format (x, y), but retrieved in the format map[y][x]
#         [0]  [1]  [2]  [3]  [4]  [5]  [6]  [7]  [8]
# map = [["x", "x", "x", "x", "x", "x", "x", "x", "x"], map[0]
#        ["x", " ", " ", " ", " ", " ", " ", " ", "x"], map[1]
#        ["x", " ", " ", " ", "x", " ", " ", " ", "x"], map[2]
#        ["x", " ", " ", " ", "x", " ", " ", " ", "x"], map[3]
#        ["x", " ", " ", " ", "x", " ", " ", " ", "x"], map[4]
#        ["x", " ", "x", " ", "x", " ", " ", " ", "x"], map[5]
#        ["x", " ", " ", " ", " ", " ", " ", " ", "x"], map[6]
#        ["x", "x", "x", "x", "x", "x", "x", "x", "x"]] map[7]

def findLowestFScore(openList, finalPos):
    lowestCoord = openList[0]
    for coordPair in openList:
        if coordPair.getFScore(finalPos) <= lowestCoord.getFScore(finalPos):
            lowestCoord = coordPair
    return lowestCoord


def aStarSearch(map, startingPos, finalPos):  # Returns a list of coordinatePair objects from starting position to ending
    openList = [startingPos]
    closedList = []
    allPathsChecked = False

    while not allPathsChecked:

        currentSquare = findLowestFScore(openList, finalPos)  # Gets square with lowest F value
        closedList.append(currentSquare)  # Adds current square to closed list and removes it
        openList.remove(currentSquare)
        if currentSquare.x == finalPos.x and currentSquare.y == finalPos.y:
            break
        adjacentSquares = findAdjacentSquares(map, currentSquare)
        for square in adjacentSquares:
            if square in closedList:
                continue
            if square not in openList:
                openList.append(square)
            else:
                if square.getFScore(finalPos) < square.getFScore(finalPos, currentSquare.gScore + 1):
                    square.parent = currentSquare
                    square.gScore = currentSquare.gScore + 1

        if len(openList) == 0:
            allPathsChecked = True
            print("No valid paths")

    successfulPath = nodeHeritage(closedList[len(closedList) - 1], [])
    successfulPath.reverse()
    return successfulPath


def findAdjacentSquares(map, currentPos):
    validMoves = []
    if map[currentPos.y + 1][currentPos.x] == " ":
        validMoves.append(CoordinatePair(currentPos.x, currentPos.y + 1, currentPos))
    if map[currentPos.y - 1][currentPos.x] == " ":
        validMoves.append(CoordinatePair(currentPos.x, currentPos.y - 1, currentPos))
    if map[currentPos.y][currentPos.x - 1] == " ":
        validMoves.append(CoordinatePair(currentPos.x - 1, currentPos.y, currentPos))
    if map[currentPos.y + 1][currentPos.x - 1] == " ":
        validMoves.append(CoordinatePair(currentPos.x - 1, currentPos.y + 1, currentPos))
    if map[currentPos.y - 1][currentPos.x - 1] == " ":
        validMoves.append(CoordinatePair(currentPos.x - 1, currentPos.y - 1, currentPos))
    if map[currentPos.y][currentPos.x + 1] == " ":
        validMoves.append(CoordinatePair(currentPos.x + 1, currentPos.y, currentPos))
    if map[currentPos.y + 1][currentPos.x + 1] == " ":
        validMoves.append(CoordinatePair(currentPos.x + 1, currentPos.y + 1, currentPos))
    if map[currentPos.y - 1][currentPos.x + 1] == " ":
        validMoves.append(CoordinatePair(currentPos.x + 1, currentPos.y - 1, currentPos))
    return validMoves


def nodeHeritage(node, nodePath):
    if node.parent is None:
        nodePath.append(node)
        return nodePath
    else:
        nodePath.append(node)
        nodeHeritage(node.parent, nodePath)
        return nodePath




def printPath(pathList):
    for step in pathList:
        step.printCoordinate()


class CoordinatePair:

    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent
        if parent is None:
            self.gScore = 0
        else:
            self.gScore = parent.gScore + 1

    def __getHScore(self, finalPos, straightLineCost=1, diagonalCost=1):
        distanceX = math.fabs(self.x - finalPos.x)
        distanceY = math.fabs(self.y - finalPos.y)
        return straightLineCost * max(distanceX, distanceY) + (diagonalCost - straightLineCost) * min(distanceX,
                                                                                                      distanceY)

    def getFScore(self, finalPos, gScore=-1):
        if gScore == -1:
            return self.gScore + self.__getHScore(finalPos)
        else:
            return gScore + self.__getHScore(finalPos)

    def printCoordinate(self):
        print(f"({self.x}, {self.y})")


if __name__ == "__main__":
    print("Main Function")

    map = [["x", "x", "x", "x", "x", "x", "x", "x", "x"],
           ["x", " ", " ", " ", "x", " ", " ", " ", "x"],
           ["x", " ", "x", " ", "x", " ", " ", " ", "x"],
           ["x", " ", "x", " ", "x", " ", " ", " ", "x"],
           ["x", " ", "x", " ", "x", " ", " ", " ", "x"],
           ["x", " ", "x", " ", "x", " ", " ", " ", "x"],
           ["x", " ", "x", " ", " ", " ", " ", " ", "x"],
           ["x", "x", "x", "x", "x", "x", "x", "x", "x"]]

    #         [0]  [1]  [2]  [3]  [4]  [5]  [6]  [7]  [8]
    # map = [["x", "x", "x", "x", "x", "x", "x", "x", "x"], map[0]
    #        ["x", " ", " ", " ", " ", " ", " ", " ", "x"], map[1]
    #        ["x", " ", " ", " ", "x", " ", " ", " ", "x"], map[2]
    #        ["x", " ", " ", " ", "x", " ", " ", " ", "x"], map[3]
    #        ["x", " ", " ", " ", "x", " ", " ", " ", "x"], map[4]
    #        ["x", " ", "x", " ", "x", " ", " ", " ", "x"], map[5]
    #        ["x", "o", " ", " ", " ", "0", " ", " ", "x"], map[6]
    #        ["x", "x", "x", "x", "x", "x", "x", "x", "x"]] map[7]

    startingPos = CoordinatePair(1, 6)
    finalPos = CoordinatePair(5, 6)

    fastestPath = aStarSearch(map, startingPos, finalPos)
    printPath(fastestPath)
