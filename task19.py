#todo: Напишите калькулятор (простой). На вход подается строка, например:
# 1 + 2  или  5 – 3  или  3 * 4  или  10 / 2.
# Вывод: сосчитать и напечатать результат операции.
# Гарантируется, что два операнда и операция есть в каждой строчке, и все они разделены пробелами.

def plus(operand1, operand2):
    return operand1 + operand2

def minus(operand1, operand2):
    return operand1 - operand2

def multiple(operand1, operand2):
    return operand1 * operand2

def divide(operand1, operand2):
    return operand1 / operand2

operationList = {"+":plus, "-":minus, "*":multiple, "/":divide}

def parse(string):
    return string.split(" ")

def calc(str):
    operand1, operation, operand2 = parse(str)
    print(str,"=",operationList[operation](int(operand1), int(operand2)))

def main():
    calc("1 + 5")
    calc("1 - 4")
    calc("2 * 2")
    calc("6 / 2")
    calc("7 / 3")

main()


