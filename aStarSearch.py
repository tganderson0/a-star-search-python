import math

# G is the movement cost from the start point A to the current square
# H is the estimated movement cost from the current square to the destination
# Coordinates are in the format (x, y), but retrieved in the format map[y][x]


class AStarSearch:
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

    def __init__(self, startPtX, startPtY, endPtX, endPtY, map):
        self.startingPos = self.CoordinatePair(startPtX, startPtY)
        self.finalPos = self.CoordinatePair(endPtX, endPtY)
        self.map = map
        self.shortestPath = self.aStarSearch()

    def findLowestFScore(self, openList):
        lowestCoord = openList[0]
        for coordPair in openList:
            if coordPair.getFScore(self.finalPos) <= lowestCoord.getFScore(self.finalPos):
                lowestCoord = coordPair
        return lowestCoord

    def aStarSearch(self):  # Returns a list of coordinatePair objects from starting position to ending
        openList = [self.startingPos]
        closedList = []
        allPathsChecked = False

        while not allPathsChecked:

            currentSquare = self.findLowestFScore(openList)  # Gets square with lowest F value
            closedList.append(currentSquare)  # Adds current square to closed list and removes it
            openList.remove(currentSquare)
            if currentSquare.x == self.finalPos.x and currentSquare.y == self.finalPos.y:
                break
            adjacentSquares = self.findAdjacentSquares(currentSquare)
            for square in adjacentSquares:
                if square in closedList:
                    continue
                if square not in openList:
                    openList.append(square)
                else:
                    if square.getFScore(self.finalPos) < square.getFScore(self.finalPos, currentSquare.gScore + 1):
                        square.parent = currentSquare
                        square.gScore = currentSquare.gScore + 1

            if len(openList) == 0:
                allPathsChecked = True
                print("No valid paths")

        successfulPath = self.nodeHeritage(closedList[len(closedList) - 1], [])
        successfulPath.reverse()
        return successfulPath

    def findAdjacentSquares(self, currentPos):
        validMoves = []
        if self.map[currentPos.y + 1][currentPos.x] == " ":
            validMoves.append(self.CoordinatePair(currentPos.x, currentPos.y + 1, currentPos))
        if self.map[currentPos.y - 1][currentPos.x] == " ":
            validMoves.append(self.CoordinatePair(currentPos.x, currentPos.y - 1, currentPos))
        if self.map[currentPos.y][currentPos.x - 1] == " ":
            validMoves.append(self.CoordinatePair(currentPos.x - 1, currentPos.y, currentPos))
        if self.map[currentPos.y + 1][currentPos.x - 1] == " ":
            validMoves.append(self.CoordinatePair(currentPos.x - 1, currentPos.y + 1, currentPos))
        if self.map[currentPos.y - 1][currentPos.x - 1] == " ":
            validMoves.append(self.CoordinatePair(currentPos.x - 1, currentPos.y - 1, currentPos))
        if self.map[currentPos.y][currentPos.x + 1] == " ":
            validMoves.append(self.CoordinatePair(currentPos.x + 1, currentPos.y, currentPos))
        if self.map[currentPos.y + 1][currentPos.x + 1] == " ":
            validMoves.append(self.CoordinatePair(currentPos.x + 1, currentPos.y + 1, currentPos))
        if self.map[currentPos.y - 1][currentPos.x + 1] == " ":
            validMoves.append(self.CoordinatePair(currentPos.x + 1, currentPos.y - 1, currentPos))
        return validMoves

    def nodeHeritage(self, node, nodePath):
        if node.parent is None:
            nodePath.append(node)
            return nodePath
        else:
            nodePath.append(node)
            self.nodeHeritage(node.parent, nodePath)
            return nodePath

    def printPath(self):
        for step in self.shortestPath:
            step.printCoordinate()



