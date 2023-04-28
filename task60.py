# Назовем пароль хорошим, если
#
# его длина равна 9 или более символам
# в нем присутствуют большие и маленькие буквы любого алфавита
# в нем имеется хотя бы одна цифра
# Напишите программу, которая требует ввода нового пароля до тех пор, пока не будет введен хороший.
#
#
# На вход программе подается произвольное количество паролей, каждый на отдельной строке. Гарантируется, что среди них присутствует хороший.
#
#
# Для каждого введенного пароля программа должна вывести текст:
#
# LengthError, если длина введенного пароля меньше 9 символов
# LetterError, если в нем все буквы имеют одинаковый регистр
# DigitError, если в нем нет ни одной цифры
# Success!, если введенный пароль хороший
#
# После ввода хорошего пароля все последующие пароли должны игнорироваться.
# Примечание 1. Приоритет вывода сообщений об ошибке в случае невыполнения нескольких условий:
# LengthError, затем LetterError, а уже после DigitError.
#
#
# Sample Input 1:
#
# arr1
# Arrrrrrrrrrr
# arrrrrrrrrrrrrrr1
# Arrrrrrr1
# Sample Output 1:
#
# LengthError
# DigitError
# LetterError
# Success!
#
# Sample Input 2:
#
# beegeek
# Beegeek123
# Beegeek2022
# Beegeek2023
# Beegeek2024
# Sample Output 2:
# LengthError
# Success!

class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

class CheckPasswords:
    def checkList(self, list_passwords):
        for password in list_passwords.split("\n"):
            try:
                self._check_password(password)
            except LengthError as e:
                print("LengthError")
            except LetterError as e:
                print("LetterError")
            except DigitError as e:
                print("DigitError")
            else:
                print("Success!")
                break


    def _validate_length(self, password):
        if len(password) < 9:
            raise LengthError()
            return False
        else:
            return True

    def _validate_letter(self, password):
        for letter in password:
            if letter.isupper():
                return True
        raise LetterError()

    def _validate_digit(self, password):
        for letter in password:
            if letter.isdigit():
                return True
        raise DigitError()

    def _check_password(self, password):
        return (self._validate_length(password) and
                self._validate_letter(password) and
                self._validate_digit(password))

checker = CheckPasswords()

print("\nSample Input 1:\n")
checker.checkList("""arr1
Arrrrrrrrrrr
arrrrrrrrrrrrrrr1
Arrrrrrr1""")

print("\nSample Input 2:\n")
checker.checkList("""beegeek
Beegeek123
Beegeek2022
Beegeek2023
Beegeek2024""")