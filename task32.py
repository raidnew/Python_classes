#todo: Дан генетический код ДНК (строка, состоящая из букв G, C, T, A)
# Постройте РНК, используя принцип замены букв: G → C, C → G, T → A, A→T.
# Напишите функцию, которая на вход получает ДНК, и возвращает РНК. Например:
#Ввод: GGCTAA
#Вывод: CCGATT

mapChange = {"G": "C", "C": "G", "T": "A", "A": "T"}

inputCode = "GGCTAA"

print("".join(list(map(lambda letter: mapChange[letter], inputCode))))