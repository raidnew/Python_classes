#todo: Дан список из кортежей (Фамилия, премия). Напечатать эти кортежи в порядке убывания премии.
# Тех, у кого одинаковая премия, то печатать в алфавитном порядке.
#  Пример ввода:
# [(Иванов, 100), (Петров, 200), (Сидоров, 200), (Воробьев, 100), (Лунин, 200)]
# Вывод:
#     Лунин 200
#     Петров 200
#     Сидоров 200
#     Воробьев 100
#     Иванов 100
#
#     Примечание:
#     https://pythonist.ru/lyambda-funkczii-dlya-sortirovki-razlichnyh-spiskov-v-python/
from functools import cmp_to_key

lst = [("Иванов", 100), ("Петров", 200), ("Сидоров", 200), ("Воробьев", 100), ("Лунин", 200)]

def compare(person1, person2):
    if(person2[1] > person1[1]): return 1
    if(person2[1] < person1[1]): return -1
    if(person2[0] > person1[0]): return -1
    return 0

lst = sorted(lst, key=cmp_to_key(compare))

for person in lst:
    print(person[0],person[1])