#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.

testArr = [4,5,7,9,12,32]
index = 0

for val in testArr:
    testArr[index] = val + 1
    index += 1

print(testArr)