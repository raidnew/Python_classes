#todo:
# Создайте функцию-генератор, которая создает последовательность числовых
# палиндромов: 1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 101 111 121 131 141 151 161 171 181 191 202 212 …

def palindrom(x):
    strx = str(x)
    for i in range(len(strx)//2):
        if(strx[i] != strx[-1 - i]):
            return False
    return True

def palindrom_generator(max):
    return [x for x in range(max) if palindrom(x)]

print(palindrom_generator(300))