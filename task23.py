# todo: На вход подается список, состоящий из списков чисел, например: [[1,5,3], [2,44,1,4], [3,3]].
#  Отсортируйте этот список по возрастанию общего количества цифр в каждом списке.
#  Каждый список отсортируйте по убыванию.

arrTest = [[1,5,3], [2,44,1,4], [3,3]]

def sortLength(arr):
    arr.sort(reverse=True)
    return len(arr)


def main():
    arrTest.sort(key=sortLength)

main()

print(arrTest)