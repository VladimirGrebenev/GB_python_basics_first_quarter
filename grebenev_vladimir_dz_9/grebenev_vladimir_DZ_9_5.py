# Домашняя работа к уроку №9 задание 5
# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод
# должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
import pickle


class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск писанины {self.title}'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск черчения {self.title}'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск подчёркивания {self.title}'

new_list_draw = Stationary('pen')
print(new_list_draw.draw())
new_pen = Pen('red pen')
print(new_pen.draw())
black_pencil = Pencil('black pencil')
print(black_pencil.draw())
yellow_handle = Handle('yellow handle')
print(yellow_handle.draw())