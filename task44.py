#todo: Напишите программу, в которой используется две функции. В одной программа «спит» 2 секунды, в другой – 3 секунды. Пусть каждая функция возвращает время, которое она «проспала».
# Главная программа запускает цикл от 0 до 10, если число четное, то запускает функцию с 2 секундами, если нечетное, то функцию с 3 секундами. Накапливает сон обеих функций отдельно и печатает две суммы.
import time

def sleep(time_sleep):
    start = time.time() * 1000.0
    time.sleep(time_sleep)
    stop = time.time() * 1000.0
    return stop - start

def main():
    summ_lag = {}
    for i in range(10):
        if i % 2 == 0:
            time_sleep = 2
        else:
            time_sleep = 3

        print("Slepping %s second" % time_sleep)
        real_sleep_time = sleep(time_sleep)

        if(str(time_sleep) in summ_lag):
            summ_lag[str(time_sleep)] += real_sleep_time
        else:
            summ_lag[str(time_sleep)] = real_sleep_time

    print(summ_lag)

main()
