# todo:
#  Напишите рекурсивную функцию sumn(n), которая вычисляет и печатает сумму чисел от 0 до n.
from functools import reduce

def sumn(n):
    print(reduce(lambda a,b: a+b, range(0, n+1)))

sumn(8)