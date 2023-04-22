#todo:
# В Python существуют ключевые слова, которые нельзя использовать для названия переменных, функций и классов. Для получения списка всех ключевых слов можно воспользоваться атрибутом kwlist из модуля keyword. Приведенный ниже код:
# import keyword
# print(keyword.kwlist)
# выводит: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# Напишите программу, которая принимает строку текста и заменяет в ней все ключевые слова на <kw>.

import keyword

test_string_with_keyword = "sklidjhFalsefalseandAndclassClassclAssasas";

def replace_keywords(string):
    found = True
    while(found):
        found = False
        for word in keyword.kwlist:
            if(word in string):
                found = True
                string = string.replace(word, "kw", 1)
    return string

print(replace_keywords(test_string_with_keyword))