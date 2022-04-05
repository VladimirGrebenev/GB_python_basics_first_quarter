# # Geek University Python-разработки - первая четверть - Основы языка Python.
# # Домашняя работа к уроку №8 задание 4
# Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения
# функции и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
# Примечание: сможете ли вы замаскировать работу декоратора?

def val_checker(x=0):
    def _val_checker(func):
        def wrapper(args):
            result = func(args)
            if lambda x: x > 0:
                if args > 0:
                    msg = result
                else:
                    msg = f'wrong val {args}'
            return msg
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

print(calc_cube(5))
print(calc_cube(-5))
