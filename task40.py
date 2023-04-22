# todo: Создайте функцию, которая принимает два аргумента, год и месяц, и возвращает list comprehension,
# содержащий все даты этого месяца в этом году. Используйте функцию monthrange(year, month) из модуля
# calendar для нахождения числа дней в месяце.
from calendar import monthrange

week_days = ("monday", "tuesday", "wensedday", "thursday", "friday", "saturday", "sunday")

def test(year = 2000, month = 1):
    start_week_day, days_lst = monthrange(year, month)
    return [(date + 1, week_days[(start_week_day + date) % 7]) for date in range(days_lst)]

print(test(2023, 4))