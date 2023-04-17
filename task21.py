#todo:  Напишите программу, которая получает на вход строку, и определяет,
# является ли строка панграммой (т.е. содержатся ли в ней все 33 буквы русского алфавита).

#word = "ыфваыфвпфывауцкавып"
word = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def check(word):
    letterNotInWord = False
    for letter in map(chr, range(*map(ord,['а', 'я']))):
        if letter not in word:
            letterNotInWord = True
            return False
    return True

print("PANAGRAM") if check(word.lower()) else print("NOT")
