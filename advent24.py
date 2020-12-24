dictOfCoords = { "ne": [1,1], "nw": [-1,1], "se": [1,-1],"sw": [-1,-1],"e": [2,0],"w": [-2,0] }

def giveLastCoordinateOfStringCommands(stringCommand):
    currentCoordinate = [0,0]
    i=0
    while i < len(stringCommand):
        if stringCommand[i] == "n" or stringCommand[i] == "s":
            for k in range(2):
                currentCoordinate[k] += dictOfCoords[stringCommand[i] + stringCommand[i+1]][k]
            i += 1
        else:
            for k in range(2):
                currentCoordinate[k] += dictOfCoords[stringCommand[i]][k]
        i +=1
    return currentCoordinate

def calculateSum(coords):
    return len(filterSurplus(coords))

def calculateNextDay(currentCoordinates):
    checkedCoordinates = []
    nextCoordinates = []
    for coordinate in currentCoordinates:
        if coordinate in checkedCoordinates: continue # already checked the coordinate
        allAdjecentCoordinates = [[coordinate[0] + x[0], coordinate[1] + x[1]] for _, x in dictOfCoords.items()]
        adjecentHexagonAmount = getAdjecentHexagonAmount(currentCoordinates[:], coordinate[:])
        if 0 < adjecentHexagonAmount < 3:
            nextCoordinates.append(coordinate[:])
        for coord in allAdjecentCoordinates:
            if not (coord in currentCoordinates) and not (coord in checkedCoordinates): #we don't want to do black hexagons here neither already checked ones
                sum = getAdjecentHexagonAmount(currentCoordinates, coord)
                if sum == 2: nextCoordinates.append(coord)
                checkedCoordinates.append(coord[:])
        checkedCoordinates.append(coordinate[:])
    return nextCoordinates

def getAdjecentHexagonAmount(currentCoordinates, hexagonCoordinates):
    sum = 0
    for _, coordinate in dictOfCoords.items():
        tempCoordinate = hexagonCoordinates[:]
        for i in range(2): tempCoordinate[i] += coordinate[i]
        if tempCoordinate in currentCoordinates: sum += 1
    return sum

def filterSurplus(coordinates):
    final = []
    i = 0
    while i < len(coordinates):
        if not coordinates[i] in coordinates[:i]:
            if (coordinates.count(coordinates[i]) & 0b1) == 0b1:
                final.append(coordinates[i])
        i += 1
    return final

def calculateDays(coordinates, days):
    nextDay = coordinates[:]
    for i in range(days):
        nextDay = calculateNextDay(nextDay)
        print("Day {}: {} ".format(i+1, calculateSum(nextDay)))


f = open("input", "r")
flippedCoordinates = []
for line in f:
    flippedCoordinates.append(giveLastCoordinateOfStringCommands(line.replace('\n', '')))
filtered = filterSurplus(flippedCoordinates)
calculateDays(filtered, 100)
