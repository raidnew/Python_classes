#todo:
# Каждый третий четверг каждого месяца билеты в Эрмитаж бесплатны. Напечатайте список дат в 2023 году, когда вход бесплатен.
import itertools
from calendar import monthrange

COUNT_MONTH = 12
COUNT_DAYS_IN_WEEK = 7
FREE_DAY_INDEX = 3
FREE_DAY_NUM = 3

def get_free_date(check_year = 2023):
    free_date_lst = []
    for month in range(COUNT_MONTH):
        day_count = 0
        for day in range(monthrange(check_year, month + 1)[1]):
            if((day + monthrange(check_year, month + 1)[0]) % COUNT_DAYS_IN_WEEK == FREE_DAY_INDEX):
                day_count += 1
                print(day,"  ",(day + monthrange(check_year, month + 1)[0]) % COUNT_DAYS_IN_WEEK)
                if(day_count == 2):
                    free_date_lst.append((month, day))
    return free_date_lst;

print(get_free_date(2023))

