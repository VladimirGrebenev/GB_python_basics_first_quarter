# # Geek University Python-разработки - первая четверть - Основы языка Python.
# # Домашняя работа к уроку №5 задание 4
# Представлен список чисел. Необходимо вывести те его элементы, значения которых больше
# предыдущего, например:
# © geekbrains.ru 13
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
# Подсказка: использовать возможности python, изученные на уроке. Подумайте, как можно
# сделать оптимизацию кода по памяти, по скорости.
import sys

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result_1 = [src[i] for i in range(1, len(src)) if src[i] > src[i-1]]
print(type(result_1), sys.getsizeof(result_1), result_1)

result = (src[i] for i in range(1, len(src)) if src[i] > src[i-1])
print(type(result), sys.getsizeof(result),[*result])
