# # Geek University Python-разработки - первая четверть - Основы языка Python.
# # Домашняя работа к уроку №1 задание 1
# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн
# <h> час <m> мин <s> сек.
# Примеры:
#
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек
#
# Примечание: можете проверить себя, подумайте, можно ли использовать цикл для проверки работы
# кода сразу для нескольких значений продолжительности, будет ли тут полезен список?
from time import strftime, gmtime

duration = input('Введите продолжительности времени через запятую: ')
duration_list = [el.strip() for el in duration.split(',')]
format_time_dict = {}

for el in duration_list:
    if int(el) < 60:
        format_time_dict[el] = strftime("%S сек", gmtime(int(el)))
    elif int(el) > 60 and int(el) < 3600:
        format_time_dict[el] = strftime("%M мин %S сек", gmtime(int(el)))
    elif int(el) > 3600 and int(el) < 86400:
        format_time_dict[el] = strftime("%H час %M мин %S сек", gmtime(int(el)))
    else:
        format_time_dict[el] = strftime("%d дн %H час %M мин %S сек", gmtime(int(el)-86400))

for key, value in format_time_dict.items():
    print(f'{key}\n{value}')
