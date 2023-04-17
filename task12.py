# Написать игру "Поле чудес"
"""
Отгадываемые слова и описание лежат в разных  массивах по одинаковому индексу.
words = ["оператор", "конструкция", "объект"]
desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования", "..", ".." ]
Пользователю выводится определение слова и количество букв в виде шаблона. Стиль шаблона может быть любым.
Слово из массива берется случайным порядком. Принимая из ввода букву мы ее открываем
в случае успеха а в случае неуспеха насчитывам штрафные балы. Игра продолжается до 10 штрафных баллов
либо победы.

Пример вывода:

"Это слово обозначает наименьшую автономную часть языка программирования"

▒  ▒  ▒  ▒  ▒  ▒  ▒  ▒

Введите букву: O

O  ▒  ▒  ▒  ▒  ▒  O  ▒


Введите букву: Я

Нет такой буквы.
У вас осталось 9 попыток !
Введите букву:
"""
import random
wordsArr = ["word1", "letters2"]
descriptionArr = ["descript word1", "description letters2"]
arrayLetters = []
arraySolvedLetters = []
currentIndex = -1
wordIsSolved = False
maxTryCount = 10
tryCount = 0

def checkWord(letter):
    global wordIsSolved
    newLetterFound = -1
    outStr = ""
    if letter not in arrayLetters:
        arrayLetters.append(newLetter)
    else:
        return 0

    for letter in wordsArr[currentIndex]:
        if(letter in arrayLetters):
            if(letter not in arraySolvedLetters):
                newLetterFound = 1
                arraySolvedLetters.append(letter)
            outStr += " "+letter
        else:
            outStr += " ▒"
    print(outStr)
    return newLetterFound


currentIndex = random.randint(0, len(wordsArr) - 1)
print(descriptionArr[currentIndex])

while wordIsSolved != True:
    newLetter = input("Введите букву:")
    if len(newLetter) != 1 : continue #Что-то не то введено
    #TODO assert letter
    letterFound = checkWord(newLetter)
    tryCount += 1
    if letterFound == -1:
        print("Нет такой буквы. У вас осталось %d попыток !" % (maxTryCount - tryCount))
    elif letterFound == 0:
        print("Буква уже была. У вас осталось %d попыток !" % (maxTryCount - tryCount))

    if tryCount >= maxTryCount:
        print("Повезет в следующий раз")
        break

