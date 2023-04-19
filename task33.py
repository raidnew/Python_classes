# todo:
#     Напишите программу, которая определяет и печатает «похожие» слова. Слово называется похожим на другое слово,
#     если его гласные буквы находятся там же, где находятся гласные буквы другого слова, например:
#     дорога и пароход - похожие слова (гласные буквы на втором, четвертом и шестом местах),
#     станок и прыжок - похожие слова, питон и удав непохожие слова.
#     Считаем, что в русском языке 10 гласных букв (а, у, о, ы, и, э, я, ю, ё, е).
#     Ввод: x –первое слово, например, питон. n – количество слов для сравнения, например 6.
#     Дальше вводятся 6 слов, например: поросенок, титан, итог, лавка, погост, кино.
#     Вывод - слова, похожие на питон: титан, погост, кино
from Tools.demo.spreadsheet import ljust

vowelsLetters = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']

#baseword = input()
#countCheckWords = int(input())
#arrWords = []

#for i in range(0, countCheckWords):
#    arrWords.append(input())

baseword = "питон"
arrWords = ["поросенок", "титан", "итог", "лавка", "погост", "кино"]

def checkLikeWords(word1, word2):
    maxLen = max(len(word1), len(word2))
    word1 = word1.ljust(maxLen)
    word2 = word2.ljust(maxLen)
    for letters in zip(word1, word2):
        if((letters[0] in vowelsLetters and letters[1] in vowelsLetters) or (letters[0] not in vowelsLetters and letters[1] not in vowelsLetters)):
            pass
        else:
            break
    else: return True
    return False
    #print(list(map(lambda l1: (l1[0] in vowelsLetters and l1[1] in vowelsLetters), zip(word1, word2))))

likeWords = []
notLikeWords = []

for word in arrWords:
    print(baseword, word)
    if(checkLikeWords(baseword, word)):
        likeWords.append(word)
    else:
        notLikeWords.append(word)

print("слова, похожие на %s :" % baseword, ", ".join(likeWords))
