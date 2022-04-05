# # Geek University Python-разработки - первая четверть - Основы языка Python.
# # Домашняя работа к уроку №7 задание 4
# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи
# — верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов
# (в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей
# (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
import os
import some_data

root_dir = some_data.__path__[0]
n100 = 0
n1000 = 0
n10000 = 0
n100000 = 0

for root, dirs, files in os.walk(root_dir):
    for file in files:
        path_file = os.path.join(root_dir, file)
        file_size = os.stat(path_file).st_size

        if file_size <= 100:
            n100 += 1
        elif 100 < file_size < 1000:
            n1000 += 1
        elif 1000 < file_size < 10000:
            n10000 += 1
        else:
            n100000 += 1

    size_dict = {100: n100, 1000: n1000, 10000: n10000, 100000: n100000, }

print(size_dict)
