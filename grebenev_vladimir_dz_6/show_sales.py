# # Geek University Python-разработки - первая четверть - Основы языка Python.
# # Домашняя работа к уроку №6 задание 6
from sys import argv

with open('bakery.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    if len(argv) == 2:
        start = int(argv[1]) - 1
        for line in lines[start:]:
            print(line.replace('\n', ''))
    elif len(argv) == 3:
        start = int(argv[1]) - 1
        stop = int(argv[2])
        for line in lines[start:stop]:
            print(line.replace('\n', ''))
    else:
        for line in lines:
            print(line.replace('\n', ''))

