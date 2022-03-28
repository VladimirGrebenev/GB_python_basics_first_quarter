# # Geek University Python-разработки - первая четверть - Основы языка Python.
# # Домашняя работа к уроку №5 задание 1
# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...

def odd_nums(max_num):
    for num in range(1, max_num+1, 2):
        yield num

odd_to_15 = odd_nums(15)
print(*odd_to_15)

