# Домашняя работа к уроку №11 задание 2
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class OwnError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'OwnError, {self.message}'
        else:
            return f'Вызван класс ошибки OwnError'

d1 = 100
d2 = 0

try:
    res = d1 / d2
except Exception:
    print(OwnError('на ноль делить нельзя'))
else:
    print(f"Все хорошо. Результат: {res}")
finally:
    print("Программа завершена")


