
import csv

def generateStartMap(size):
    startingMap = []
    for counter in range(size):
        currentLine = []
        for counter in range(size):
            currentLine.append("~")
        startingMap.append(currentLine)

    return startingMap


def shotToNumbers(coordinateString, headingsList):
    shotList = []
    shotList.append(int(coordinateString[1]))

    for column in headingsList:
        if coordinateString[0] == column:
            shotList.append(headingsList.index(column))

    return shotList


def checkHit(shot, map):
    if map[shot[0]][shot[1]] == "O":
        return ["X", "Miss!"]
    elif map[shot[0]][shot[1]] == "B":
        return ["B", "ЕСТЬ ПРОБИТИЕ КОРОБЛЯ!"]
    elif map[shot[0]][shot[1]] == "S":
        return ["S", "ЕСТЬ ПРОБИТИЕ ПОДВОДНОЙ ЛОДКИ!"]



def updateMap(lastShotCell, lastShotResult, map):
    map[lastShotCell[0]][lastShotCell[1]] = lastShotResult
    return map


def checkShipStatus(shipList, shipMap):
    shipStatus = []
    for index in range(len(shipList)):
        shipStatus.append(False)
    for index in range(len(shipList)):
        for list in shipMap:
            if shipList[index] in list:
                shipStatus[index] = True
    return shipStatus

# --- Game variables ---
gridSize = 10
validRows = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
validColumns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
shipSymbols = ["B", "S", "D", "C"]
shipNames = ["КОРАБЛЬ", "ПОДВОДНАЯ ЛОДКА"]
playing = True


print("---------------------------\n"
      "       КОРАБЛЬ\n"
      "---------------------------\n")

print("Велком ту зе грэйтест гэйм оф ол тайм нэймд МОРСКОЙ БОЙ""!\n"
      "Тут на карте есть враги, типа\n"
      "здесь короче 4 боевых коробля\n"
      "и ещё подводная лодка\n"
      "у тебя есть карта моря\n"
      "амуниция не беснонечна, так что стреляй с умом\n"
      "на этом всё, УДАЧИ!\n"
      "---------------------------\n")


while playing:

    fileName = "battleshipMap.txt"
    accessMode = "r"
    shipMap = []

    try:
        with open(fileName, accessMode) as fileData:
            shipLocations = csv.reader(fileData)
            for row in shipLocations:
                shipMap.append(row)
    except FileNotFoundError:
        print("произошла ошибка при загрузке файла")

    while True:
        difficulty = input("на какой сложности будешь играть? (easy/hard) ").lower()
        if difficulty == "easy":
            missileCount = 50
            break
        elif difficulty == "hard":
            missileCount = 35
            break
        else:
            print("выбери доступную сложность")

    currentMap = generateStartMap(gridSize)
    previousShots = []

    while missileCount > 0:

        print("---------------------------")
        print("  " + " ".join(validColumns))
        for counter in range(gridSize):
            print(str(counter) + " " + " ".join(currentMap[counter]))

        print("---------------------------\n"
              "осталось зарядов" + str(missileCount))

        while True:
            userShot = input("введи координаты, куда будешь стрелять").upper()
            if len(userShot) != 2:
                print("введи координаты:")
            elif userShot in previousShots:
                print("мы уже сюда стреляли, выбери другое место")
            elif userShot[0] not in validColumns or userShot[1] not in validRows:
                print("координаты за пределами диапазона.")
            else:
                previousShots.append(userShot)
                shotCoordinateList = shotToNumbers(userShot, validColumns)
                break

        print("---------------------------")

        shotResult = checkHit(shotCoordinateList, shipMap)
        print(shotResult[1])

        shipMap = updateMap(shotCoordinateList, "X", shipMap)
        shipsStillAlive = checkShipStatus(shipSymbols, shipMap)
        for index in range(len(shipsStillAlive)):
            if shipsStillAlive[index]:
                print(" " + shipNames[index] + " всё ещё на плаву!")
            else:
                print("ТЫ ПОТОПИЛ" + shipNames[index] + "!")

        currentMap = updateMap(shotCoordinateList, shotResult[0], currentMap)


        if True not in shipsStillAlive:
            print("ХОРОШ! Ты потопил все корабли врага")
            break


        missileCount -= 1
        if missileCount == 0:
            print("Похоже, вражеский флот смог уплыть. Увы")

    print("---------------------------")
    userContinue = input("Хочешь сыграть ещё? (Y/N) ").upper()
    while True:
        if userContinue == "Y":
            playing = True
            break
        elif userContinue == "N":
            playing = False
            break
        else:
            print("Я не понимаю, что ты ввел, извини. Попробуй ввести Y или N")
