#todo:
# Определите класс Person. При создании объекта p=Person(‘Иванов’, ‘Михаил’, ‘Федорович’) необходимо ввести полное имя человека.
# При печати объекта должно выводиться следующее:
# print(p) # чивородеФлиахиМвонавИ

class Person:
    first_name = ""
    second_name = ""
    third_name = ""

    def __init__(self, *args, **kwargs):
        self.first_name = args[1] or ""
        self.second_name = args[0] or ""
        self.third_name = args[2] or ""

    def __str__(self):
        return ''.join(reversed(self.second_name+self.first_name+self.third_name))

p=Person("Иванов", "Михаил", "Федорович")
print(p)