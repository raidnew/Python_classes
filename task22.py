# todo: Напишите функцию, которая шифрует строку, содержащую латинские буквы с помощью шифра Цезаря. Каждая буква сдвигается на заданное число n позиций вправо. Пробелы, знаки препинания не меняются. Например, для n = 1.
# a → b,   b → c,    p → q,    y → z,    z V a
# A → B,   B → C,   Z → A
# Т.е. заголовок функции будет def code(string, n):
# В качестве результата печатается сдвинутая строка.

tableCode = "abcdefghijklmnopqrstuvwxyz";


def code(string, n):
    retData = [];
    for letter in string:
        upper = letter.isupper()
        letter = letter.lower()
        newIndex = (tableCode.find(letter) + n) % len(tableCode)
        newLetter = tableCode[newIndex]
        if upper:
            retData.append(newLetter.upper())
        else:
            retData.append(newLetter)

    return "".join(retData)


def main():
    print(code("abctreSDzZ", 2));


main()
