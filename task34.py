# todo:
#  Напишите рекурсивную функцию sumn(n), которая вычисляет и печатает сумму чисел от 0 до n.
from functools import reduce

def sumn_old(n):
    print(reduce(lambda a,b: a+b, range(0, n+1)))

def sumn(n):
    if(n > 0):
        return n + sumn(n-1)
    return 0

print(sumn(8))