# todo: Десериализация
# Напишите программу, которая принимает на вход название JSON файла, десериализует содержащийся в этом файле объект и выводит его.
#
# если файла с данным названием нет в папке с программой, программа должна вывести текст:
# Файл не найден
# если файл с данным названием содержит некорректные данные (то есть не удовлетворяющие формату JSON), программа должна вывести текст:
# Ошибка при десериализации
#
# На вход программе подается название JSON файла.
#
#
# Программа должна десериализовать объект, содержащийся в файле с введенным названием, и вывести его. Если при поиске файла или десериализации его содержимого произошла ошибка, программа должна вывести соответствующий текст.
#
# Примечание 1. Название подаваемого файла уже содержит расширение.
#
# Примечание 2. Тестируемый файл numbers.json имеет следующее содержание
#
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
import json
from json import JSONDecodeError


# numbers.json
# Sample Output 1:
#
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#
# Ошибка при десериализации

class JSONParser:

    file = None
    data = None

    def load(self, file_name = "test59.json"):
        try:
            self.file = open(file_name, "r")
        except FileNotFoundError as e:
            print(f"File {file_name} not found ")
        except Exception as e:
            print("Error ",e)
        else:
            print(f"file {file_name} load complete")

    def parse(self):
        if(self.file):
            try:
                self.data = json.load(self.file)
            except JSONDecodeError as e:
                print("Ошибка при десериализации: ", e)
            except TypeError as e:
                print(e)
            except Exception as e:
                print(e)
            else:
                print("Parse complete")
                return True
        else:
            print("File not loaded")
        return False


parser = JSONParser()
parser.load("test59.json")
if(parser.parse()): print(parser.data)
print("\n")
parser2 = JSONParser()
parser2.load("test59er.json")
if(parser2.parse()): print(parser2.data)