from aStarSearch import AStarSearch
import time
import os
import sys

def animatePath(pathList, map, finalX, finalY):
    originalMap = map
    originalMap[finalY][finalX] = "3"
    for step in pathList:
        clear()
        tempMap = originalMap
        printMapWithLocation(tempMap, step.x, step.y)
        time.sleep(0.5)
    input()


def printMapWithLocation(tempMap, currentX, currentY):

    tempMap[currentY][currentX] = "o"
    for line in tempMap:
        tempLine = ""
        for element in line:
            if element == "x":
                tempLine += "◻"
            else:
                tempLine += element
        print(tempLine)
    tempMap[currentY][currentX] = " "


def clear():
    os.system('cls')


def runFromMap(map):
    startX = -1
    startY = -1
    finalX = -1
    finalY = -1

    currentY = 0
    for line in map:
        currentX = 0
        for element in line:
            if element == "o":
                startX = currentX
                startY = currentY
                map[currentY][currentX] = " "
            elif element == "3":
                finalX = currentX
                finalY = currentY
                map[currentY][currentX] = " "
            currentX += 1
        currentY += 1

    if startX == -1 or finalX == -1:
        raise NotImplementedError("The starting position or final position is missing")

    tempSearch = AStarSearch(startX, startY, finalX, finalY, map)
    animatePath(tempSearch.shortestPath, map, finalX, finalY)
    return


def mapFromFile(fileName):
    with open(fileName) as file:
        tempMap = []
        for line in file.readlines():
            tempLine = []
            for character in line:
                tempLine.append(character)
            if "\n" in tempLine:
                tempLine.remove("\n")
            tempMap.append(tempLine)
    return tempMap


if __name__ == "__main__":

    map = [["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
           ["x", " ", " ", " ", " ", " ", "x", "o", "x", " ", " ", " ", " ", " ", "x"],
           ["x", " ", "x", "x", "x", " ", "x", " ", "x", "x", "x", "x", "x", " ", "x"],
           ["x", " ", "x", " ", "x", " ", "x", " ", " ", " ", " ", " ", "x", " ", "x"],
           ["x", " ", "x", " ", "x", " ", "x", "x", "x", "x", "x", " ", "x", " ", "x"],
           ["x", " ", "x", " ", " ", " ", " ", " ", " ", " ", " ", " ", "x", " ", "x"],
           ["x", "x", "x", " ", "x", "x", " ", "x", "x", "x", "x", "x", "x", " ", "x"],
           ["x", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
           ["x", " ", "x", "x", "x", " ", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
           ["x", " ", "x", " ", "x", " ", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
           ["x", " ", "x", " ", "x", " ", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
           ["x", " ", " ", " ", "x", " ", " ", " ", " ", " ", " ", " ", " ", " ", "x"],
           ["x", "x", "x", "x", "x", " ", "x", " ", " ", " ", " ", " ", " ", " ", "x"],
           ["x", " ", " ", " ", "x", " ", "x", " ", " ", " ", " ", " ", " ", " ", "x"],
           ["x", " ", "x", "x", "x", " ", "x", "x", " ", " ", " ", " ", " ", " ", "x"],
           ["x", " ", " ", " ", " ", " ", " ", " ", "3", " ", " ", " ", " ", " ", "x"],
           ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]]

    runFromMap(mapFromFile(sys.argv[1]))
