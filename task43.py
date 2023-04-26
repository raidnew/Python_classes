#todo:
# Каждый третий четверг каждого месяца билеты в Эрмитаж бесплатны. Напечатайте список дат в 2023 году, когда вход бесплатен.
import itertools
import calendar
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

COUNT_MONTH = 12
COUNT_DAYS_IN_WEEK = 7
FREE_DAY_INDEX = 4
FREE_DAY_NUM = 3

def get_free_date(check_year = 2023):
    free_date_lst = []
    for month in range(COUNT_MONTH):
        day_count = 0
        for day in range(1, calendar.monthrange(check_year, month + 1)[1]):
            if((day + calendar.monthrange(check_year, month + 1)[0]) % COUNT_DAYS_IN_WEEK == FREE_DAY_INDEX):
                day_count += 1
                if(day_count == FREE_DAY_NUM):
                    free_date_lst.append((month, day))
    return free_date_lst;

months = [name for name in calendar.month_name if name]

free_dates = get_free_date(2023)

for date in free_dates:
    print("%s %d" % (months[date[0]], date[1]))

