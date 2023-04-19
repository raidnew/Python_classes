#todo: Реализовать игровую механику морского боя.
# 1. Система в случайном порядке расставляет 10 однопалубных кораблей в игровом поле 10x10
# 2. Между караблями при расстановке должно соблюдаться правило пустых полей.
# 3. Игра заканчивается при 20 промахах.
import os
import random

field = []
rows = []
cols = []

cellType = {"EMPTY":0, "SHIP":1, "CRUSH":2, "BROKEN":3, "BUSY": 4}

lockCellNearShip = ((-1, -1),(-1, 0),(-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1))

def generateEmptyField(size):
    retField = []

    rows = list(range(1, size+1))
    cols = list(map(chr, range(ord("A"), ord("A") + size)))

    for iy in range(0, size):
        retField.append([])
        for ix in range(0, size):
            retField[iy].append(cellType["EMPTY"])

    return rows, cols, retField

def installShips(shipCount):
    global field
    count = 0
    while count < shipCount:
        y = random.randrange(0, len(field))
        x = random.randrange(0, len(field[y]))
        if allowInstallShip(x, y) == True:
            count += 1
            installShip(x, y)

    #drawField()


def allowInstallShip(x, y):
    if cellInField(x, y) == False: return False
    return getFieldCell(x, y) == cellType['EMPTY']

def installShip(x, y):
    setFieldCell(x, y, cellType['SHIP'])
    cellsBusy = list(map(lambda offset: (y + offset[1], x + offset[0]), lockCellNearShip))
    for cell in cellsBusy:
        setFieldCell(cell[1], cell[0], cellType['BUSY'])

def getFieldCell(x, y):
    global field
    return field[y][x]

def setFieldCell(x, y, cell):
    global field
    if(cellInField(x, y)):
        field[y][x] = cell

def cellInField(x ,y):
    global field
    if y < 0: return False
    if y >= len(field): return False
    if x < 0: return False
    if x >= len(field[y]): return False
    return True

def drawField():
    global field, rows, cols
    letterMap = "    "
    letterMapUnder = "    "
    for letter in cols:
        letterMap += " "+letter+" "
        letterMapUnder += "---"
    print(letterMap)
    print(letterMapUnder)
    for line, number in zip(field, rows):
        strField = str(number).rjust(2) + " |"
        for cell in line:
            cellShow = "░"
            match(cell):
                case 0:
                    cellShow = "░"
                case 1:
                    cellShow = "8"#"░"
                case 2:
                    cellShow = "o"
                case 3:
                    cellShow = "X"
                case 4:
                    cellShow = "░"
            #cellShow = str(cell)
            strField += " "+cellShow+" "
        print(strField)

def shoot(row, col):
    isHit = False
    try:
        x = cols.index(col)
        y = rows.index(int(row))
        newCell = 2
        match(getFieldCell(x, y)):
            case 0:
                newCell = 2
            case 1:
                isHit = True
                newCell = 3
            case 2:
                newCell = 2
            case 3:
                newCell = 3
            case 4:
                newCell = 2
        setFieldCell(x,y,newCell)
    except:
        print("Invalid coordinates")
    return isHit

def startGame(missCount, shipCount):
    endGame = False
    win = False
    while(not endGame):
        drawField()
        print("Осталось %d промахов" % missCount)
        row = input("Номер строки: ")
        col = input("Буква стобца: ")
        if not shoot(row, col.upper()):
            missCount -= 1
        else:
            shipCount -= 1
        if(missCount == 0):
            endGame = True
            break

        if(shipCount == 0):
            endGame = True
            win = True
            break

    if(win):
        print("вы победили")
    else:
        print("Вы проиграли")


def main():
    global field, rows, cols
    rows, cols, field = generateEmptyField(10)
    installShips(10)
    startGame(20, 10)

main()


