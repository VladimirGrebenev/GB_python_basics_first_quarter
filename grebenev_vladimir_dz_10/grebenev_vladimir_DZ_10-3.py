# Домашняя работа к уроку №10 задание 3
# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число). В классе должны быть реализованы
# методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только к
# клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого)
# деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек
# исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек
# двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как произведение
# количества ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное
# деление количества ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество
# ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно
# переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются
# все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()
# вернёт строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернёт
# строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.

class Cell:
    def __init__(self, number_of_slots):
        self.number_of_slots = int(number_of_slots)

    def __add__(self, other):
        slots = self.number_of_slots + other.number_of_slots
        return  Cell(slots)

    def __sub__(self, other):
        slots = self.number_of_slots - other.number_of_slots
        if slots > 0:
            return Cell(slots)
        else:
            return "если вычесть эти клетки, то ничего не останется"

    def __mul__(self, other):
        slots = self.number_of_slots * other.number_of_slots
        return Cell(slots)

    def __truediv__(self, other):
        slots = (self.number_of_slots + other.number_of_slots) // 2
        return Cell(slots)

    def make_order(self, slots_in_row):
        # return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])
        row_number = self.number_of_slots // slots_in_row
        last_row_slots = self.number_of_slots % slots_in_row
        matrix = [['*' for j in range(slots_in_row)] for i in range(row_number)]
        last_row_list = ['*' for i in range(last_row_slots)]
        matrix.append(last_row_list)
        return '\n'.join([''.join([i for i in row]) for row in matrix])

a = Cell(2)
b = Cell(21)
c = a.__add__(b)
print(c)
print(c.number_of_slots)
d = a.__sub__(b)
print(d)
print(type(d))
f = b.__mul__(a)
print(f.number_of_slots)
g = b.__truediv__(a)
print(g.number_of_slots)
result = b.make_order(5)
print(result)

