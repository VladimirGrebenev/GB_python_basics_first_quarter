# # Geek University Python-разработки - первая четверть - Основы языка Python.
# # Домашняя работа к уроку №8 задание 3
# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
# # @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

def type_logger(func):
    def wrapper(*args, **kwargs):
        log = func(*args, **kwargs)
        return f'{log}: {type(log)}'

    return wrapper

@type_logger
def calc_cube(x):
   return x ** 3

print(calc_cube(5))

